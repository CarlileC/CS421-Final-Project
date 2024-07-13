from flask import Flask, render_template, request
from markupsafe import Markup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/CoffeeList')
def CoffeeList():
    return render_template('CoffeeList.html')

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
