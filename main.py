import os
from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from coffeeInfo import descriptionChoice
from utilities import passwordCheck
from flask_login import LoginManager, UserMixin, login_user, logout_user

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQL_TRAC_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "TEMP KEY"
db = SQLAlchemy(app)

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
    
    def __init__(self, firstName, lastName, password, email):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        
    def __repr__(self):
        return f"ID: {self.id} Name: {self.firstName} {self.lastName} Email: {self.email} Password: {self.password}"
    
# class Coffee(db.Model):
#     _tablename__="Coffee"
    
#     id = db.Column(db.Integer, primary_key = True)
#     coffeeName = db.Column(db.Text)
#     favCount = db.Column(db.Integer)
    
#END SECTION

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
    if request.method == "POST": #User submits the form
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.session.query(User).filter(User.email==email, User.password==password).first() #queries the database, looking if there is a combination in the database
        if user is not None: #Is there a user? If so log them in
            login_user(user)
            return redirect(url_for('secretpage'))
        else: #No? Let them try again and give them an error
            return render_template('signin.html', errorMessage=Markup("<h2>Incorrect username or password"))

    return render_template('signin.html') #User clicks on the nav bar link

#Still a little messy
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST": #User submits the form
        firstName:str = request.form.get('firstName')
        lastName:str = request.form.get('lastName')
        email:str = request.form.get('email')
        password:str = request.form.get('password')
        confirmPassword:str = request.form.get('confirmPassword')
        
        passwordInfo:list = passwordCheck(password, confirmPassword) #located in utilities, checks if password meets requirements
        
        if passwordInfo[0]: #password met requirements!
            try:
                newUser:User = User(firstName, lastName, password, email)
                db.session.add(newUser)
                db.session.commit()
                return redirect(url_for('signin', errorMessage="Thank you, please sign in")) #redirects them to the sign in page, letting them know it worked
            except IntegrityError:
                return render_template('signup.html', errorMessage=Markup("<h3 class='errorMessage'>Email already in database</h3>")) #email in database, try again
        else: #password failed, error message located in second element of list.
            return render_template('signup.html', errorMessage=passwordInfo[1])
        
    return render_template("signup.html") #User clicks on the nav bar link

#A fun reference, should be removed later
@app.route('/secretpage', methods=['GET', 'POST'])
def secretpage():
        return render_template('secretpage.html', message=Markup(f"<h1>My name is Chris Houlihan. <br> This is my top secret page. <br> Keep it between us, OK?</h1>"))

@app.route("/signout")
def signout():
    logout_user()
    return redirect(url_for("index"))

#Renders the coffee list
@app.route('/cart')
def cart():
    coffeeImage = Markup("<img src='https://m.media-amazon.com/images/I/81nV6x2ey4L._AC_UF1000,1000_QL80_.jpg'>")
    return render_template('cart.html', coffeeImage=coffeeImage)

@app.route('/CoffeeList')
def CoffeeList():
    return render_template('CoffeeList.html')


#I hate the function I made to clean this up. Is there a better way?
#descriptionChoice located in coffeeInfo.py
@app.route('/SecondBreakfast')
def SecondBreakfast():
    infoList = descriptionChoice("Second Breakfast")

    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], coffeeDropdown=infoList[3])


@app.route('/TheRoastOfLeaves')
def TheRoastOfLeaves():
    infoList = descriptionChoice("The Roast of Leaves")

    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], coffeeDropdown=infoList[3])

@app.route('/AtTheCupsOfMadness')
def AtTheCupsOfMadness():
    infoList = descriptionChoice("At the Cups of Maddness")

    return render_template('CoffeePage.html', coffeeName=infoList[0], coffeeImage=infoList[1], coffeeDescription=infoList[2], coffeeDropdown=infoList[3])
    
if __name__ == "__main__":
    app.run(debug=True)

#source activate coffeeshop