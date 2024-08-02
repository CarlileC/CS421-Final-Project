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
        coffee_description = "Venture across The Water and into The Hill and enjoy a nice cup of coffee with your second breakfast (just mind your head, \
            hobbits are quite short compared to us but they would love your company). Enjoy the stories of the brave hobbits leaving the shire. The Baggins and the Tooks are peculear ones, \
             aren't they? Why would anyone venture across The Water instead of nibbling on a biscuit while enjoying the earthy flavors of this roast of coffee and watching the sun rise \
            over The Hill? Well why don't you make yourself a cup and read the story by the grandfather of fantasy."
    elif name == "The Roast of Leaves":
        coffee_image = 'https://m.media-amazon.com/images/I/51QoJuZLrlL._AC_UF1000,1000_QL80_.jpg'
        coffee_description = "This Roast was not made for you </br></br> A roast darker than the labyrinth in the Navidson house with bold flavors rivaling depth \
        of the four day long staircase. Enjoy while reading about the horrors that awaited the Navidsons when they moved into their new house. How would you feel \
        if your house suddenly had a hallway that could not logically exist? Would you explore? Would you run? Could you truly call that house a home? Sit down and make a cup, \
        you'll need it if you ever want to make it out.</br></br> \
        Disclaimer: C & M Media Coffee is not responsible for any minotaur encountered after drinking this roast."
    elif name == "Mercer's Blend":
        coffee_image = 'https://m.media-amazon.com/images/I/91E9fEdeW1L._AC_UF1000,1000_QL80_.jpg'
        coffee_description = "Feeling down? Tired of the polluted atmosphere? Can't afford a real animal so you have to buy an electric one? A cup of Mercer's Blend \
        is just what you need to start the day. One taste of this citrusy blend will fill you with warmth and tranquility. You will feel at peace and in tune with the rest \
        of humanity. While you're at it, read about the bounty hunter Rick Decard as he fights to rid Earth of rogue androids. <br> <br>\
        WARNING: If someone you know drinks this blend and does not feel a rush of empathy and connection to the rest of humanity, run and contact the police immediately!"
    elif name == 'The Silverhand Special':
        coffee_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkQGrg6m1XJQPJ1GMyG3DRYNqIw7krFaWgIA&s'
        coffee_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    elif name == 'Western Nostalgia':
        coffee_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW69ccLk0atQA_ikEKj_06IcvAX8bRjAPyIw&s'
        coffee_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    elif name == 'Potion of Energy':
        coffee_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6DKnP8m8EHbfT7f5L6ixqAvHiHQxxhFtkZg&s'
        coffee_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse non volutpat nunc. Sed vitae diam quis sapien venenatis consequat vitae a est.  \
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo enim, tristique eu erat non, ullamcorper rutrum felis. \
         Suspendisse quis laoreet libero. Maecenas dolor dolor, convallis ac mi et, vulputate fermentum erat. Sed leo tortor, dictum ut accumsan sed, mattis in dui. \
         Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ullamcorper dui quis lacinia sodales. \
          Integer a leo sed lorem facilisis pharetra sit amet id risus. Morbi metus eros, feugiat sit amet massa et, elementum rutrum libero. \
          Suspendisse id leo nec metus egestas sodales vitae vitae felis. Vivamus accumsan vulputate luctus. Praesent ut finibus lectus. \
          Donec vitae mauris at diam maximus sollicitudin."
    info_list = [name, coffee_image ,coffee_description]
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
    elif name == "Mercer's Blend":
        return Markup("<a href='/MercersBlend'><img src='https://m.media-amazon.com/images/I/91E9fEdeW1L._AC_UF1000,1000_QL80_.jpg'> \
            <p>Mercer's Blend</p> \
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