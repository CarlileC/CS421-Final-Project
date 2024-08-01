from markupsafe import Markup


'''
description_choice takes in the name of a coffee and renders it's description and image appropriately
This function is messy, but with how each coffee has a long description, drop down menu, and image, this 
could not be avoided since these are too long to store into a database the only other option would to have
seperate .html files for each coffee but that is also messy in its own right so we went with this
'''
def description_choice(name:str):
    if name == "Second Breakfast":
        coffee_image = 'https://m.media-amazon.com/images/I/81nV6x2ey4L._AC_UF1000,1000_QL80_.jpg'
        coffee_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
        coffee_dropdown = Markup("<option value='Second Breakfast'>Second Breakfast</option> \
                            <option value='Lord of the Rings'>Lord of the Rings</option> \
                            <option value='Second Breakfast + Lord of the Rings'>Second Breakfast + Lord of the Rings</option>")
    elif name == "The Roast of Leaves":
        coffee_image = Markup("<img src='https://m.media-amazon.com/images/I/51QoJuZLrlL._AC_UF1000,1000_QL80_.jpg'>")
        coffee_dropdown = Markup("<option value='The Roast of Leaves'>The Roast of Leaves</option> \
                                <option value='The House of Leaves'>The House of Leaves</option> \
                                <option value='The Roast of Leaves + The House of Leaves'>The Roast of Leaves + The House of Leaves</option>")
        coffee_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
            Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
            Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
            Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
            Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
            Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
            Donec vitae mauris at diam maximus sollicitudin."
    elif name == "At the Cups of Madness":
        coffee_image = Markup("<img src='https://m.media-amazon.com/images/I/71aD7mGX+2L._AC_UF1000,1000_QL80_.jpg'>")
        coffee_dropdown = Markup("<option value='At the Cups of Madness'>At the Cups of Madness</option> \
                            <option value='At the Mountains of Madness'>At the Mountains of Madness</option> \
                            <option value='At the Cups of Madness + At the Mountains of Madness'>At the Cups of Madness + At the Mountains of Madness</option>")
        coffee_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    elif name == 'The Silverhand Special':
        coffee_image = Markup("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkQGrg6m1XJQPJ1GMyG3DRYNqIw7krFaWgIA&s'>")
        coffee_dropdown = Markup("<option value='Silverhand Special'>The Silverhand Special</option> \
                                <option value='Cyberpunk 2077'>Cyberpunk 2077</option>")
        coffee_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    elif name == 'Western Nostalgia':
        coffee_image = Markup("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW69ccLk0atQA_ikEKj_06IcvAX8bRjAPyIw&s'>")
        coffee_dropdown = Markup("<option value='Western Nostalgia'>Western Nostalgia</option> \
                                <option value='Red Dead Redemption 2'>Red Dead Redemption 2</option>")
        coffee_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    elif name == 'Potion of Energy':
        coffee_image = Markup("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6DKnP8m8EHbfT7f5L6ixqAvHiHQxxhFtkZg&s'>")
        coffee_dropdown = Markup("<option value='Potion of Energy'>Potion of Energy</option> \
                                <option value='Minecraft'>Minecraft</option>")
        coffee_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    info_list = [name, coffee_image ,coffee_description, coffee_dropdown]
    return info_list

def popular_picks(name:str):
    if name == "Second Breakfast":
        return Markup("<a href='/SecondBreakfast'><img src='https://m.media-amazon.com/images/I/81nV6x2ey4L._AC_UF1000,1000_QL80_.jpg'> \
            <p>Second Breakfast</p> \
            </a>") 
    elif name == "The Roast of Leaves":
        return Markup("<a href='/TheRoastOfLeaves'><img src='https://m.media-amazon.com/images/I/51QoJuZLrlL._AC_UF1000,1000_QL80_.jpg'> \
            <p>The Roast of Leaves</p> \
            </a>") 
    elif name == "At the Cups of Madness":
        return Markup("<a href='/AtTheCupsOfMadness'><img src='https://m.media-amazon.com/images/I/71aD7mGX+2L._AC_UF1000,1000_QL80_.jpg'> \
            <p>At The Cups of Madness</p> \
            </a>") 
    elif name == "The Silverhand Special":
        return Markup("<a href='/TheSilverhandSpecial'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkQGrg6m1XJQPJ1GMyG3DRYNqIw7krFaWgIA&s'> \
            <p>The Silverhand Special</p> \
            </a>") 
    elif name == "Western Nostalgia":
        return Markup("<a href='/WesternNostalgia'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW69ccLk0atQA_ikEKj_06IcvAX8bRjAPyIw&s'> \
            <p>Western Nostalgia</p> \
            </a>") 
    elif name == "Potion of Energy":
        return Markup("<a href='/PotionOfEnergy'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6DKnP8m8EHbfT7f5L6ixqAvHiHQxxhFtkZg&s'> \
            <p>Potion of Energy</p> \
            </a>") 