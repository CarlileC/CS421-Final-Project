from main import db, User, Coffee, Favorite, Book, VideoGame
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

# newCoffee3 = Coffee("Second Breakfast", 0, 25.00)
# newCoffee = Coffee("At The Cups of Madness", 0, 25.00)
# newCoffee2 = Coffee("The Roast of Leaves", 0, 25.00)

# db.session.add(newCoffee3)
# db.session.add(newCoffee)
# db.session.add(newCoffee2)
# db.session.commit()
#This would normally be current_user_id = current_user.id


user = db.session.query(Book).all()

# db.session.query(Favorite).filter(Favorite.user_id == current_user.id, Favorite.coffee_id == coffee_to_fav.id).first()
print(user)