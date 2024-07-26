import os
from flask import Flask, render_template, redirect, session, url_for
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from coffeeInfo import descriptionChoice
from utilities import passwordCheck
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, EqualTo

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQL_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "TEMP KEY"
db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

#THIS NEXT SECTION IS JUST TAKEN FROM LAB07, IT NEEDS TO BE CLEANED UP AND MOVED INTO A DIFFERENT FILE IDEALLY
class User(UserMixin, db.Model):
    __tablename__="Users"
    
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    password = db.Column(db.Text)
    email = db.Column(db.Text, unique = True)
    cart = db.relationship('Cart', backref='user', uselist=False, lazy=True) 
    """
    line 34 creates a relationship between the user and the cart, backref='user' essentially creates a user attribute for the cart which lets a cart object access
    a user, uselist=False makes it a one-to-one relationship with cart, lazy=True means that cart items won't be loaded unless the cart is accessed
    """
    
    def __init__(self, firstName, lastName, password, email):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        
    def __repr__(self):
        return f"ID: {self.id} Name: {self.firstName} {self.lastName} Email: {self.email} Password: {self.password}"
    

"""
line 56, line 68, line76 creates a new column that allows item to be attached to a cart id (db.ForeignKey('Cart.id'))
(if i am understanding it correctly)
"""    
class Coffee(db.Model):
    __tablename__="Coffee"
    
    id = db.Column(db.Integer, primary_key = True)
    coffeeName = db.Column(db.Text, nullable = False)
    favCount = db.Column(db.Integer)
    price = db.Column(db.Float, nullable = False)
    cart_id = db.Column(db.Integer, db.ForeignKey('Cart.id'), nullable=True)
    cart = db.relationship('Cart', back_populates='coffeeItems')

class Book(db.Model):
    __tablename__="Book"

    id = db.Column(db.Integer, primary_key = True)
    bookName = db.Column(db.Text, nullable = False)
    price = db.Column(db.Float, nullable = False)
    cart_id = db.Column(db.Integer, db.ForeignKey('Cart.id'), nullable=True)
    cart = db.relationship('Cart', back_populates='bookItems')

class VideoGame(db.Model):
    __tablename__="Videogame"

    id = db.Column(db.Integer, primary_key = True)
    gameName = db.Column(db.Text, nullable = False)
    price = db.Column(db.Float, nullable = False)
    cart_id = db.Column(db.Integer, db.ForeignKey('Cart.id'), nullable=True)
    cart = db.relationship('Cart', back_populates='gameItems')

class Cart(db.Model):
    __tablename__="Cart"

    
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    coffeeItems = db.relationship('Coffee', back_populates="cart", lazy=True)
    bookItems = db.relationship('Book', back_populates='cart', lazy=True)
    gameItems = db.relationship('VideoGame', back_populates='cart', lazy=True)
    """
    line 84 creates the link between the user and the cart just like in the 'product' models
    lines 85-87 create the cart attributes for each 
    """

with app.app_context():
    db.create_all()
#END SECTION

"""
The forms for the signin and signup methods
"""
class SignInForm(FlaskForm):
    email = StringField('Email:', validators = [InputRequired()])
    password = PasswordField('Password:', validators = [InputRequired()])
    submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
    email = StringField('Email:', validators = [InputRequired()])
    password = PasswordField('Password:', validators = [InputRequired()])
    confirmPassword = PasswordField('Confirm Password:', validators=[InputRequired(), EqualTo('password', message='Passwords must be the same')])
    firstName = StringField('First Name:', validators = [InputRequired()])
    lastName = StringField('Last Name:', validators = [InputRequired()])

"""Lord of the Rings"""
class SelectLotrItemsForm(FlaskForm):
    product_choice = SelectField(choices=['Second Breakfast', 'The Lord of the Rings'])
    submit = SubmitField('Add to Cart')

"""House of Leaves"""
class SelectHoLItemsForm(FlaskForm):
    product_choice = SelectField(choices=['Roast of Leaves', 'House of Leaves'])
    submit = SubmitField('Add to Cart')

"""At the House of Madness"""
class SelectAtHoMItemsForm(FlaskForm):
    product_choice = SelectField(choices=['At the Cups of Madness', 'At the Mountains of Madness'])
    submit = SubmitField('Add to Cart')

@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)

#Renders the home page
@app.route('/')
def index():
    return render_template('index.html')


#Sign In
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit(): #User submits the form
        email = form.email.data
        password = form.password.data
        user = db.session.query(User).filter(User.email==email, User.password==password).first() #queries the database, looking if there is a combination in the database
        if user is not None: #Is there a user? If so log them in
            login_user(user)
            return redirect(url_for('secretpage'))
        else: #No? Let them try again and give them an error
            return render_template('signin.html', errorMessage=Markup("<h2>Incorrect username or password"), form=form)

    return render_template('signin.html', form=form) #User clicks on the nav bar link

#Still a little messy
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit(): #User submits the form
        firstName:str = form.firstName.data
        lastName:str = form.lastName.data
        email:str = form.email.data
        password:str = form.password.data
        confirmPassword:str = form.confirmPassword.data
        
        passwordInfo:list = passwordCheck(password, confirmPassword) #located in utilities, checks if password meets requirements
        
        if passwordInfo[0]: #password met requirements!
            try:
                newUser = User(firstName=firstName, lastName=lastName, password=password, email=email)
                db.session.add(newUser)
                db.session.flush()  # Ensure the user ID is available
                
                # Create a cart for the new user
                newCart = Cart(user_id=newUser.id)
                db.session.add(newCart)
                
                # Commit the transaction
                db.session.commit()
                return redirect(url_for('signin', errorMessage="Thank you, please sign in")) #redirects them to the sign in page, letting them know it worked
            except IntegrityError:
                return render_template('signup.html', errorMessage=Markup("<h3 class='errorMessage'>Email already in database</h3>")) #email in database, try again
        else: #password failed, error message located in second element of list.
            return render_template('signup.html', errorMessage=passwordInfo[1])
        
    return render_template("signup.html", form=form) #User clicks on the nav bar link

#A fun reference, should be removed later
@app.route('/secretpage', methods=['GET', 'POST'])
def secretpage():
        return render_template('secretpage.html', message=Markup(f"<h1>My name is Chris Houlihan. <br> This is my top secret page. <br> Keep it between us, OK?</h1>"))

@app.route("/signout")
def signout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/cart')
@login_required
def cart():
    if current_user:
        user_cart = current_user.cart
        user_coffee_items = user_cart.coffeeItems
        user_book_items = user_cart.bookItems
        user_game_items = user_cart.gameItems
        return render_template('cart.html', current_user=current_user, user_coffee_items=user_coffee_items, user_book_items=user_book_items, user_game_items=user_game_items)
    else:
        return render_template('SecretPage.html')

# renders the cart

@app.route('/CoffeeList')
def CoffeeList():
    return render_template('CoffeeList.html')

#Renders the coffee list

#I hate the function I made to clean this up. Is there a better way?
#descriptionChoice located in coffeeInfo.py
@app.route('/SecondBreakfast', methods=['GET', 'POST'])
def SecondBreakfast():
    coffeeDropDown = SelectLotrItemsForm()
    infoList = descriptionChoice("Second Breakfast")
    print(current_user.cart)
    if coffeeDropDown.validate_on_submit():
        print('form validated')
        product = coffeeDropDown.product_choice.data
        if product == 'Second Breakfast':
            new_coffee = Coffee(coffeeName='Second Breakfast', favCount=0, price=19.99, cart=current_user.cart)
            db.session.add(new_coffee)
            db.session.commit()
        if product == 'The Lord of the Rings':
            print(product + ' selected.')
            new_book = Book(bookName='Lord of the Rings', price=89.99, cart=current_user.cart)
            db.session.add(new_book)
            db.session.commit()
    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], coffeeDropDown=coffeeDropDown)


@app.route('/TheRoastOfLeaves', methods=['GET', 'POST'])
def TheRoastOfLeaves():
    coffeeDropDown = SelectHoLItemsForm()
    infoList = descriptionChoice("The Roast of Leaves")
    print(current_user.cart)
    if coffeeDropDown.validate_on_submit():
        print('form validated')
        product = coffeeDropDown.product_choice.data
        if product == 'Roast of Leaves':
            new_coffee = Coffee(coffeeName='The Roast of Leaves', favCount=0, price=19.99, cart=current_user.cart)
            db.session.add(new_coffee)
            db.session.commit()
        if product == 'House of Leaves':
            new_book = Book(bookName='House of Leaves', price=29.99, cart=current_user.cart)
            db.session.add(new_book)
            db.session.commit()
    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], coffeeDropDown=coffeeDropDown)

@app.route('/AtTheCupsOfMadness', methods=['GET', 'POST'])
def AtTheCupsOfMadness():
    coffeeDropDown = SelectAtHoMItemsForm()
    infoList = descriptionChoice("At the Cups of Maddness")
    print(current_user.cart)
    if coffeeDropDown.validate_on_submit():
        print('form validated')
        product = coffeeDropDown.product_choice.data
        if product == 'At the Cups of Madness':
            new_coffee = Coffee(coffeeName='At the Cups of Madness', favCount=0, price=19.99, cart=current_user.cart)
            db.session.add(new_coffee)
            db.session.commit()
        if product == 'At the House of Madness':
            new_book = Book(bookName='At the Mountains of Madness', price=25.99, cart=current_user.cart)
            db.session.add(new_book)
            db.session.commit()
    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], coffeeDropdown=infoList[3])
    
if __name__ == "__main__":
    app.run(debug=True)

#source activate coffeeshop