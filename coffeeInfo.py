from markupsafe import Markup


#I kind of hate this 
def descriptionChoice(name:str):
    if name == "Second Breakfast":
        coffeeImage = Markup("<img src='https://m.media-amazon.com/images/I/81nV6x2ey4L._AC_UF1000,1000_QL80_.jpg'>") 
        coffeeDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
        coffeeDropdown = Markup("<option value='Second Breakfast'>Second Breakfast</option> \
                            <option value='Lord of the Rings'>Lord of the Rings</option> \
                            <option value='Second Breakfast + Lord of the Rings'>Second Breakfast + Lord of the Rings</option>")
    elif name == "The Roast of Leaves":
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
    elif name == "At the Cups of Maddness":
        coffeeImage = Markup("<img src='https://m.media-amazon.com/images/I/71aD7mGX+2L._AC_UF1000,1000_QL80_.jpg'>")
        coffeeDropdown = Markup("<option value='At the Cups of Madness'>At the Cups of Madness</option> \
                            <option value='At the House of Madness'>At the House of Madness</option>")
        coffeeDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    elif name == 'The Silverhand Special':
        coffeeImage = Markup("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkQGrg6m1XJQPJ1GMyG3DRYNqIw7krFaWgIA&s'>")
        coffeeDropdown = Markup("<option value='Silverhand Special'>The Silverhand Special</option> \
                                <option value='Cyberpunk 2077'>Cyberpunk 2077</option>")
        coffeeDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    elif name == 'Western Nostalgia':
        coffeeImage = Markup("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW69ccLk0atQA_ikEKj_06IcvAX8bRjAPyIw&s'>")
        coffeeDropdown = Markup("<option value='Western Nostalgia'>Western Nostalgia</option> \
                                <option value='Red Dead Redemption 2'>Red Dead Redemption 2</option>")
        coffeeDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    elif name == 'Potion of Energy':
        coffeeImage = Markup("<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6DKnP8m8EHbfT7f5L6ixqAvHiHQxxhFtkZg&s'>")
        coffeeDropdown = Markup("<option value='Potion of Energy'>Potion of Energy</option> \
                                <option value='Minecraft'>Minecraft</option>")
        coffeeDescription = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    infoList = [name, coffeeImage ,coffeeDescription, coffeeDropdown]
    return infoList