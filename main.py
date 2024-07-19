import os
from flask import Flask, render_template, request
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


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

#THIS SECTION ALSO NEEDS TO BE CLEANED UP PASSWORD CHECK SHOULD BE MOVED INTO A SEPERATE FUNCTION THAT RETURNS ALL THE RENDER TEMPLATES
#IDEALLY THIS FUNCTION SHOULD BE NO MORE THAN 5-10 LINES
@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    email = request.args.get('email')
    password = request.args.get('password')
    confirmPassword = request.args.get('confirmPassword')
    
    if password != confirmPassword:
        return render_template('signup.html', errorMessage=Markup("<p>Passwords did not match!</p>"))
    
    upper = False
    lower = False
    number = password[-1].isdigit()
    length = len(password) >= 8
    for i in password:
        if i.isupper() == True:
            upper = True
        elif i.islower() == True:
            lower = True
    message = "<p>Oh no! Looks like you had issues with your password! <br><br> Here are the requirements you failed:<p> <ul>"
    if(not upper):
        message += "<li>You did not use an upper case letter</li>"
    if(not lower):
        message += "<li>You did not use a lower case letter</li>"
    if(not number):
        message += "<li>You did not use a number at the end</li>"
    if(not length):
        message += "<li>Your password is less than 8 characters"
    
    if(upper and lower and number and length):
        message = "<p>Your Password passed the 3 requirements</p>"
        newUser:User = User(firstName, lastName, password, email)
        try:
            db.session.add(newUser)
            db.session.commit()
            return render_template('thankyou.html', message=Markup(f"<h3>Account successfully created! Thank you {firstName} {lastName}</h3>"))
        except IntegrityError:
                return render_template('signup.html', errorMessage=Markup("<h3>Email already in database</h3>"))
        
    else:
        message += "</ul>"
        returnMessage = Markup(message)
        return render_template('signup.html', errorMessage=returnMessage)

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

'''
All of these functions render CoffeePage.html, but dynamically change them based on the button pressed.
coffeeImage is the link to the picture used on the web page.
coffeeDropdown is for the dropdown menu, it lists 3 options. Just the coffee, just the book, then a combo of the book and the coffee
coffeeDescription is for a quick description of the coffee and how it relates to the book, as well as a quick description of the book.
'''
@app.route('/SecondBreakfast')
def SecondBreakfast():
    coffeeImage = Markup("<img src='https://m.media-amazon.com/images/I/81nV6x2ey4L._AC_UF1000,1000_QL80_.jpg'>") 
    coffeeDropdown = Markup("<option value='Second Breakfast'>Second Breakfast</option> \
                            <option value='Lord of the Rings'>Lord of the Rings</option> \
                            <option value='Second Breakfast + Lord of the Rings'>Second Breakfast + Lord of the Rings</option>")
    coffeeDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    return render_template('CoffeePage.html', coffeeName="Second Breakfast", coffeeImage=coffeeImage, coffeeDescription=coffeeDescription, coffeeDropdown=coffeeDropdown)

@app.route('/TheRoastOfLeaves')
def TheRoastOfLeaves():
    coffeeImage = Markup("<img src='https://m.media-amazon.com/images/I/51QoJuZLrlL._AC_UF1000,1000_QL80_.jpg'>")
    coffeeDropdown = Markup("<option value='The Roast of Leaves'>The Roast of Leaves</option> \
                            <option value='The House of Leaves'>The House of Leaves</option> \
                            <option value='The Roast of Leaves + The House of Leaves'>The Roast of Leaves + The House of Leaves</option>")
    coffeeDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    return render_template('CoffeePage.html', coffeeName="The Roast of Leaves", coffeeImage=coffeeImage, coffeeDescription=coffeeDescription, coffeeDropdown=coffeeDropdown)

@app.route('/AtTheCupsOfMadness')
def AtTheCupsOfMadness():
    coffeeImage = Markup("<img src='https://m.media-amazon.com/images/I/71aD7mGX+2L._AC_UF1000,1000_QL80_.jpg'>")
    coffeeDropdown = Markup("<option value='At the Cups of Madness'>At the Cups of Madness</option> \
                            <option value='At the House of Madness'>At the House of Madness</option> \
                            <option value='At the Cups of Madness + At the House of Madness'>At the Cups of Madness + At the House of Madness</option>")
    coffeeDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    return render_template('CoffeePage.html', coffeeName="At The Cups of Madness", coffeeImage=coffeeImage, coffeeDescription=coffeeDescription, coffeeDropdown=coffeeDropdown)
    
if __name__ == "__main__":
    app.run(debug=True)

#source activate coffeeshop