import os
from flask import Flask, render_template, request
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from coffeeInfo import descriptionChoice
from utilities import passwordCheck
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQL_TRAC_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#THIS NEXT SECTION IS JUST TAKEN FROM LAB07, IT NEEDS TO BE CLEANED UP AND MOVED INTO A DIFFERENT FILE IDEALLY
class User(db.Model):
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
    
db.create_all()
#END SECTION

#Renders the home page
@app.route('/')
def index():
    return render_template('index.html')

#Sign Up button routing
@app.route('/signup')
def signup():
    return render_template('signup.html')

#Sign In button routing
@app.route('/signin')
def signin():
    return render_template('signin.html')

#Still a little messy
@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    firstName:str = request.args.get('firstName')
    lastName:str = request.args.get('lastName')
    email:str = request.args.get('email')
    password:str = request.args.get('password')
    confirmPassword:str = request.args.get('confirmPassword')
    
    passwordInfo:list = passwordCheck(password, confirmPassword) #located in utilities, checks if password meets requirements
    
    if passwordInfo[0]: #password met requirements!
        try:
            newUser:User = User(firstName, lastName, password, email)
            db.session.add(newUser)
            db.session.commit()
            return render_template('thankyou.html', message=Markup(f"<h3>Account successfully created! Thank you {firstName} {lastName}</h3>"))
        except IntegrityError:
            return render_template('signup.html', errorMessage=Markup("<h3 class='errorMessage'>Email already in database</h3>"))
    else: #password failed, error message located in second element of list.
        return render_template('signup.html', errorMessage=passwordInfo[1])

#This should be fine? Still a little messy
@app.route('/secretpage', methods=['GET', 'POST'])
def secretpage():
    email = request.args.get('email')
    password = request.args.get('password')
    success = db.session.query(User).filter(User.email==email, User.password==password).first() is not None
    if success:
        return render_template('secretpage.html', message=Markup(f"<h1>You have successfully logged in</h1>"))
    else:
        return render_template('signin.html', errorMessage=Markup("<h2>Incorrect username or password"))

#END SECTION


#Renders the coffee list
@app.route('/CoffeeList')
def CoffeeList():
    return render_template('CoffeeList.html')


#I hate the function I made to clean this up. Is there a better way?

@app.route('/SecondBreakfast')
def SecondBreakfast():
    infoList = descriptionChoice("Second Breakfast") #located in coffeeInfo.py

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