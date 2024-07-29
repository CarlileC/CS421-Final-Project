from main import db, User, Coffee, Favorite
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

newCoffee = Coffee("At The Cups of Madness", 0, 25.00)
# newCoffee2 = Coffee("The Roast of Leaves", 0, 25.00)

db.session.add(newCoffee)
# db.session.add(newCoffee2)
db.session.commit()
#This would normally be current_user_id = current_user.id

print(Coffee.query.order_by(desc(Coffee.favCount)).all())