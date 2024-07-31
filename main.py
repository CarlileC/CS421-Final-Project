import os
from flask import Flask, render_template, redirect, session, url_for, jsonify
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from coffeeInfo import descriptionChoice, popularPicks
from utilities import passwordCheck, fav_or_unfav, favoriting_info, add_coffee_to_cart, add_book_to_cart, add_game_to_cart
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField
from wtforms.validators import InputRequired, EqualTo
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQL_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "TEMP KEY"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

#THIS NEXT SECTION IS JUST TAKEN FROM LAB07, IT NEEDS TO BE CLEANED UP AND MOVED INTO A DIFFERENT FILE IDEALLY

class Favorite(db.Model):
    __tablename__="Favorite"
    
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False) 
    coffee_id = db.Column(db.Integer, db.ForeignKey('Coffee.id'), nullable=False)
    #many to many relationship between user and coffee
    def __init__(self, user_id, coffee_id):
        self. user_id = user_id
        self. coffee_id = coffee_id

        
    def __repr__(self):
        return f"ID: {self.id} user_id: {self.user_id} coffee_id: {self.coffee_id}"
    
class User(UserMixin, db.Model):
    __tablename__="Users"
    
    id = db.Column(db.Integer, primary_key = True)
    firstName = db.Column(db.Text)
    lastName = db.Column(db.Text)
    password = db.Column(db.Text)
    email = db.Column(db.Text, unique = True)
    coffees = db.relationship('Coffee', secondary=Favorite.__table__, backref='Users')
    cart = db.relationship('Cart', backref='user', uselist=False, lazy=True) 
    admin = db.Column(db.Boolean, nullable=True)
    """
    line 34 creates a relationship between the user and the cart, backref='user' essentially creates a user attribute for the cart which lets a cart object access
    a user, uselist=False makes it a one-to-one relationship with cart, lazy=True means that cart items won't be loaded unless the cart is accessed
    """
    
    def __init__(self, firstName, lastName, password, email, admin):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.admin = admin
        
    def __repr__(self):
        return f"ID: {self.id} Name: {self.firstName} {self.lastName} Email: {self.email} Password: {self.password}"
    

"""
line 56, line 68, line76 creates a new column that allows item to be attached to a cart id (db.ForeignKey('Cart.id'))
(if i am understanding it correctly)
"""

class CartItem(db.Model):
    __tablename__ ='cart_items'

    id = db.Column(db.Integer, primary_key = True)
    coffee_id = db.Column(db.Integer, db.ForeignKey('Coffee.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('Book.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('Videogame.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('Cart.id'))
    quantity = db.Column(db.Integer, default = 1)
    price = db.Column(db.Integer)

class Coffee(db.Model):
    __tablename__="Coffee"
    
    id = db.Column(db.Integer, primary_key = True)
    coffeeName = db.Column(db.Text, nullable = False)
    favCount = db.Column(db.Integer)
    users = db.relationship('User', secondary=Favorite.__table__, backref='Coffee')
    stock = db.Column(db.Integer, nullable = False)
    carts = db.relationship('Cart', secondary=CartItem.__table__, back_populates='coffee_items', viewonly=True)
    
    def __init__(self, coffeeName, favCount, stock):
        self.coffeeName =coffeeName
        self.favCount = favCount
        self.stock = stock
    
    def __repr__(self):
        return f"ID: {self.id} Name: {self.coffeeName} Fav: {self.favCount}"

class Book(db.Model):
    __tablename__="Book"

    id = db.Column(db.Integer, primary_key = True)
    bookName = db.Column(db.Text, nullable = False)
    cart_id = db.Column(db.Integer, db.ForeignKey('Cart.id'), nullable=True)
    stock = db.Column(db.Integer, nullable = False)
    carts = db.relationship('Cart', secondary=CartItem.__table__, back_populates='book_items', viewonly=True)

class VideoGame(db.Model):
    __tablename__="Videogame"

    id = db.Column(db.Integer, primary_key = True)
    gameName = db.Column(db.Text, nullable = False)
    carts = db.relationship('Cart', secondary=CartItem.__table__, back_populates='game_items', viewonly=True)
    stock = db.Column(db.Integer, nullable = False)

class Cart(db.Model):
    __tablename__="Cart"
    
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    coffee_items = db.relationship('Coffee', secondary=CartItem.__table__, back_populates="carts", viewonly=True, lazy=True) 
    book_items = db.relationship('Book', secondary=CartItem.__table__, back_populates='carts', viewonly=True, lazy=True)
    game_items = db.relationship('VideoGame', secondary=CartItem.__table__, back_populates='carts', viewonly=True, lazy=True)

    """
    cart and the product models are linked by a table callted CartItems
    """


with app.app_context():
    db.create_all()

    coffee = Coffee.query.filter_by(coffeeName='Second Breakfast').first()
    if not coffee:
        db.session.add(Coffee(coffeeName='Second Breakfast', favCount=0, stock=10))
        db.session.add(Coffee(coffeeName='The Roast of Leaves', favCount=0, stock = 10))
        db.session.add(Coffee(coffeeName='At the Cups of Madness', favCount=0, stock = 10))
        db.session.add(Coffee(coffeeName='The Silverhand Special', favCount=0, stock = 10))
        db.session.add(Coffee(coffeeName='Western Nostalgia', favCount=0, stock = 10))
        db.session.add(Coffee(coffeeName='Potion of Energy', favCount=0, stock = 10))
        db.session.add(Book(bookName='The Lord of the Rings', stock = 10))
        db.session.add(Book(bookName='The House of Leaves', stock = 10))
        db.session.add(Book(bookName='At the Mountains of Madness', stock = 10))
        db.session.add(VideoGame(gameName='Cyberpunk 2077', stock = 10))
        db.session.add(VideoGame(gameName='Red Dead Redemption 2', stock = 10))
        db.session.add(VideoGame(gameName='Minecraft', stock = 10))
        db.session.commit()
    admin_login = User.query.filter_by(email="admin@coffeeshop.com", password = "admin").first() #the unsecured router classic
    if not admin_login:
        db.session.add(User(firstName="admin", lastName="admin", password="admin", email="admin@coffeeshop.com", admin=True))
        db.session.commit()


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

class FavoriteButton(FlaskForm):
    field1 = HiddenField('Favorite Button')
    submit = SubmitField('Favorite')
    
"""Lord of the Rings"""
class SelectLotrItemsForm(FlaskForm):
    product_choice = SelectField(choices=[('Second Breakfast', 'Second Breakfast'), ('The Lord of the Rings', 'The Lord of the Rings')])
    submit = SubmitField('Add to Cart')

"""House of Leaves"""
class SelectHoLItemsForm(FlaskForm):
    product_choice = SelectField(choices=[('The Roast of Leaves', 'The Roast of Leaves'), ('The House of Leaves','The House of Leaves')])
    submit = SubmitField('Add to Cart')

"""At the Mountains of Madness"""
class SelectAtMoMItemsForm(FlaskForm):
    product_choice = SelectField(choices=[('At the Cups of Madness','At the Cups of Madness'), ('At the Mountains of Madness','At the Mountains of Madness')])
    submit = SubmitField('Add to Cart')

class SelectCyberPunkItemsForm(FlaskForm):
    product_choice = SelectField(choices=[('The Silverhand Special', 'The Silverhand Special'), ('Cyberpunk 2077', 'Cyberpunk 2077')])
    submit = SubmitField('Add to Cart')

class SelectRDRItemsForm(FlaskForm):
    product_choice = SelectField(choices=[('Western Nostalgia','Western Nostalgia'), ('Red Dead Redemption 2','Red Dead Redemption 2')])
    submit = SubmitField('Add to Cart')

class SelectMCItemsForm(FlaskForm):
    product_choice = SelectField(choices=[('Potion of Energy', 'Potion of Energy'), ('Minecraft','Minecraft')])
    submit = SubmitField('Add to Cart')

class MyModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.admin:
                return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index'))

class MyAdminView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.admin:
                return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index'))

admin = Admin(app, index_view=MyAdminView())
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Coffee, db.session))
admin.add_view(MyModelView(VideoGame, db.session))
admin.add_view(MyModelView(Book, db.session))



@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)

#Renders the home page
@app.route('/')
def index():
    favorites = Coffee.query.order_by(desc(Coffee.favCount)).all()
    popular1 = popularPicks(favorites[0].coffeeName)
    popular2 = popularPicks(favorites[1].coffeeName)
    popular3 = popularPicks(favorites[2].coffeeName)
    return render_template('index.html', popular1=popular1, popular2=popular2, popular3=popular3)


#Sign In
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit(): #User submits the form
        email = form.email.data
        password = form.password.data
        user = db.session.query(User).filter(User.email==email, User.password==password).first() #queries the database, looking if there is a combination in the database
        if user is not None: #Is there a user? If so log them in
            if user.admin:
                login_user(user)
                return redirect(url_for('admin.index'))
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
                newUser = User(firstName=firstName, lastName=lastName, password=password, email=email, admin=False)
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

# renders the cart
@app.route('/cart')
@login_required
def cart():
    if current_user:
        coffee_class = Coffee
        book_class = Book
        game_class = VideoGame
        cart_items = CartItem.query.filter_by(cart_id=current_user.id)
        total = 0
        for item in cart_items:
            total = total + item.quantity * item.price
        return render_template('cart.html', total=total,
                               cart_items=cart_items,
                               coffee_class=coffee_class,
                               book_class=book_class,
                               game_class=game_class)
    else:
        return render_template('SecretPage.html')
    
@app.route("/delete-coffee/<int:coffee_id>", methods=['POST'])
@login_required
def delete_coffee(coffee_id):
    cart_item = CartItem.query.filter_by(cart_id=current_user.id, coffee_id=coffee_id).first_or_404()
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        db.session.commit()
    elif cart_item.quantity <= 1:
        db.session.delete(cart_item)
        db.session.commit()
    return redirect(url_for('cart'))

@app.route("/delete-book/<int:book_id>", methods=['POST'])
def delete_book(book_id):
    book_item = CartItem.query.filter_by(cart_id=current_user.id, book_id=book_id).first_or_404()
    if book_item.quantity > 1:
        book_item.quantity -= 1
        db.session.commit()
    elif book_item.quantity <= 1:
        db.session.delete(book_item)
        db.session.commit()
    return redirect(url_for('cart'))

@app.route("/delete-game/<int:game_id>", methods=['POST'])
def delete_game(game_id):
    game_item = CartItem.query.filter_by(cart_id=current_user.id, game_id=game_id).first_or_404()
    if game_item.quantity > 1:
        game_item.quantity -= 1
        db.session.commit()
    elif game_item.quantity <= 1:
        db.session.delete(game_item)
        db.session.commit()
    return redirect(url_for('cart'))

@app.route('/CoffeeList')
def CoffeeList():
    return render_template('CoffeeList.html')

#Renders the coffee list

#I hate the function I made to clean this up. Is there a better way?
#descriptionChoice located in coffeeInfo.py
@app.route('/SecondBreakfast', methods=['GET', 'POST'])
def SecondBreakfast():
    drop_down = SelectLotrItemsForm(prefix='cart')
    infoList = descriptionChoice("Second Breakfast")
    favorite_button = FavoriteButton(prefix='favorite')
    if current_user.is_authenticated:
        favorite_info:list = favoriting_info(db, current_user, favorite_button, Coffee, "Second Breakfast") #index 0 is current_coffee row, index 1 is the modified favorite button
        fav_unfav_button = favorite_info[1]
    else:
        fav_unfav_button = ""
    if favorite_button.validate_on_submit():
        fav_or_unfav(db, favorite_info[1], favorite_info[0], current_user, Favorite, Coffee)
        print("form submitted")
        return jsonify(data={"Favorite".format(favorite_button.submit.data)})
    elif drop_down.validate_on_submit():
        product = drop_down.product_choice.data
        if product == 'Second Breakfast':
            add_coffee_to_cart(db, 'Second Breakfast', current_user.cart, Coffee, CartItem, 19.99)
        elif product == 'The Lord of the Rings':
            add_book_to_cart(db, 'The Lord of the Rings', current_user.cart, Book, CartItem, 89.99)
    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], drop_down=drop_down, fav_unfav_button=fav_unfav_button)


@app.route('/TheRoastOfLeaves', methods=['GET', 'POST'])
def TheRoastOfLeaves():
    drop_down = SelectHoLItemsForm(prefix='cart')
    infoList = descriptionChoice("The Roast of Leaves")
    favorite_button = FavoriteButton(prefix='favorite')
    if current_user.is_authenticated:
        favorite_info:list = favoriting_info(db, current_user, favorite_button, Coffee, "The Roast of Leaves") #index 0 is current_coffee row, index 1 is the modified favorite button
        fav_unfav_button = favorite_info[1]
    else:
        fav_unfav_button = "" #If the user is not logged in, it will throw a index out of bounds error
        
    if favorite_button.validate_on_submit():
        fav_or_unfav(db, favorite_info[1], favorite_info[0], current_user, Favorite, Coffee)
        
    if drop_down.validate_on_submit():
        product = drop_down.product_choice.data
        if product == 'The Roast of Leaves':
            add_coffee_to_cart(db, 'The Roast of Leaves', current_user.cart, Coffee, CartItem, 19.99)
        elif product == 'The House of Leaves':
            add_book_to_cart(db, 'The House of Leaves', current_user.cart, Book, CartItem, 29.99)
    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], drop_down=drop_down, fav_unfav_button=fav_unfav_button)

@app.route('/AtTheCupsOfMadness', methods=['GET', 'POST'])
def AtTheCupsOfMadness():
    drop_down = SelectAtMoMItemsForm(prefix='cart')
    infoList = descriptionChoice("At the Cups of Madness")
    favorite_button = FavoriteButton(prefix='favorite')
    if current_user.is_authenticated:
        favorite_info:list = favoriting_info(db, current_user, favorite_button, Coffee, "At the Cups of Madness") #index 0 is current_coffee row, index 1 is the modified favorite button
        fav_unfav_button = favorite_info[1]
    else:
        fav_unfav_button = ""   
    if favorite_button.validate_on_submit():
        fav_or_unfav(db, favorite_info[1], favorite_info[0], current_user, Favorite, Coffee)
        fav_unfav_button = favorite_info[1]
        
    user_cart = current_user.cart
    if drop_down.validate_on_submit():
        product = drop_down.product_choice.data
        if product == 'At the Cups of Madness':
            add_coffee_to_cart(db, 'At the Cups of Madness', current_user.cart, Coffee, CartItem, 19.99)
        elif product == 'At the Mountains of Madness':
            add_book_to_cart(db, 'At the Mountains of Madness', current_user.cart, Book, CartItem, 25.99)
    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], drop_down=drop_down, fav_unfav_button=fav_unfav_button)

@app.route('/TheSilverhandSpecial', methods=['GET', 'POST'])
def silver_hand_special():
    drop_down = SelectCyberPunkItemsForm(prefix='cart')
    infoList = descriptionChoice('The Silverhand Special')
    user_cart = current_user.cart
    favorite_button = FavoriteButton(prefix='favorite')
    if current_user.is_authenticated:
        favorite_info:list = favoriting_info(db, current_user, favorite_button, Coffee, "The Silverhand Special") #index 0 is current_coffee row, index 1 is the modified favorite button
        fav_unfav_button = favorite_info[1]
    else:
        fav_unfav_button = "" #If the user is not logged in, it will throw a index out of bounds error
        
    if favorite_button.validate_on_submit():
        fav_or_unfav(db, favorite_info[1], favorite_info[0], current_user, Favorite, Coffee)
        
    if drop_down.validate_on_submit():
        product = drop_down.product_choice.data
        if product == 'The Silverhand Special':
            add_coffee_to_cart(db, 'The Silverhand Special', current_user.cart, Coffee, CartItem, 19.99)
        elif product == 'Cyberpunk 2077':
            add_game_to_cart(db, 'Cyberpunk 2077', current_user.cart, VideoGame, CartItem, 59.99)
    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], drop_down=drop_down, fav_unfav_button=fav_unfav_button)

@app.route('/WesternNostalgia', methods=['GET', 'POST'])
def western_nostalgia():
    drop_down = SelectRDRItemsForm(prefix='cart')
    infoList = descriptionChoice('Western Nostalgia')
    user_cart = current_user.cart
    favorite_button = FavoriteButton(prefix='favorite')
    if current_user.is_authenticated:
        favorite_info:list = favoriting_info(db, current_user, favorite_button, Coffee, "Western Nostalgia") #index 0 is current_coffee row, index 1 is the modified favorite button
        fav_unfav_button = favorite_info[1]
    else:
        fav_unfav_button = "" #If the user is not logged in, it will throw a index out of bounds error
        
    if favorite_button.validate_on_submit():
        fav_or_unfav(db, favorite_info[1], favorite_info[0], current_user, Favorite, Coffee)
        
    if drop_down.validate_on_submit():
        product = drop_down.product_choice.data
        if product == 'Western Nostalgia':
            add_coffee_to_cart(db, 'Western Nostalgia', current_user.cart, Coffee, CartItem, 19.99)
        elif product == 'Red Dead Redemption 2':
            add_game_to_cart(db, 'Red Dead Redemption 2', current_user.cart, VideoGame, CartItem, 59.99)
    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], drop_down=drop_down, fav_unfav_button=fav_unfav_button)

@app.route('/PotionOfEnergy', methods=['GET', 'POST'])
def potion_of_energy():
    drop_down = SelectMCItemsForm(prefix='cart')
    infoList = descriptionChoice('Potion of Energy')
    user_cart = current_user.cart
    favorite_button = FavoriteButton(prefix='favorite')
    if current_user.is_authenticated:
        favorite_info:list = favoriting_info(db, current_user, favorite_button, Coffee, "Potion of Energy") #index 0 is current_coffee row, index 1 is the modified favorite button
        fav_unfav_button = favorite_info[1]
    else:
        fav_unfav_button = "" #If the user is not logged in, it will throw a index out of bounds error
        
    if favorite_button.validate_on_submit():
        fav_or_unfav(db, favorite_info[1], favorite_info[0], current_user, Favorite, Coffee)
        
    if drop_down.validate_on_submit():
        product = drop_down.product_choice.data
        if product == 'Potion of Energy':
            add_coffee_to_cart(db, 'Potion of Energy', current_user.cart, Coffee, CartItem, 19.99)
        if product == 'Minecraft':
            add_game_to_cart(db, 'Minecraft', current_user.cart, VideoGame, CartItem, 19.99)
    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], drop_down=drop_down, fav_unfav_button=fav_unfav_button)

if __name__ == "__main__":
    app.run(debug=True)
