from markupsafe import Markup


def password_check(password:str, confirm_password:str) -> list:    
        upper = False
        lower = False
        number = password[-1].isdigit()
        length = len(password) >= 8
        password_match = False
        
        for i in password:
            if i.isupper() == True:
                upper = True
            elif i.islower() == True:
                lower = True

        if password == confirm_password:
            password_match = True
    
        message = "<p>Oh no! Looks like you had issues with your password! <br><br> Here are the requirements you failed:<p> <ul class='errorMessage'>"
        
        
        
        if password != confirm_password:
            password_match = False
    
        if(not upper):
            message += "<li>You did not use an upper case letter</li>"
        if(not lower):
            message += "<li>You did not use a lower case letter</li>"
        if(not number):
            message += "<li>You did not use a number at the end</li>"
        if(not length):
            message += "<li>Your password is less than 8 characters</li>"
        if not password_match:
            message += "<li>Your passwords did not match</li>"
        
        
        if(upper and lower and number and length):
            return [True]
        else:
            message += "</ul>"
            returnMessage = Markup(message)
            return [False, returnMessage]
        

def fav_or_unfav(db, favorite_button, current_coffee, current_user, Favorite, Coffee):
    if(favorite_button.submit.label.text == "Favorite"):
        new_favorite = Favorite(user_id = current_user.id, coffee_id = current_coffee.id)
        current_coffee.favCount = Coffee.favCount + 1
        db.session.add(new_favorite)
        db.session.commit()
        favorite_button.submit.label.text = "Unfavorite"      
        print("Favorite Pressed")
        print(current_user.Coffee)
    else:
        db.session.query(Favorite).filter(Favorite.user_id == current_user.id, Favorite.coffee_id == current_coffee.id).delete()
        current_coffee.favCount = Coffee.favCount - 1
        db.session.commit()
        favorite_button.submit.label.text = "Favorite"
        print("Unfavorite Pressed")
        print(current_user.Coffee)
        
def favoriting_info(db, current_user, favorite_button, Coffee, coffee_name):
    current_coffee = db.session.query(Coffee).filter(Coffee.coffee_name==coffee_name).first()
        #These two lines are changing how the favorite button is rendered on the render_template function below
    if current_coffee not in current_user.Coffee:
        favorite_button.submit.label.text = "Favorite"
    else:
        favorite_button.submit.label.text = "Unfavorite"
    return [current_coffee, favorite_button]
        
def add_coffee_to_cart(db, coffee_name, user_cart, Coffee, CartItem, price):
    coffee = Coffee.query.filter_by(coffee_name=coffee_name).first()
    coffee_item = CartItem.query.filter_by(cart_id=user_cart.id, coffee_id=coffee.id).first()
    if coffee_item: # for quantity, check to see if an item exists already, if it does, increase the quantity
        coffee_item.quantity += 1
        db.session.commit()
    else:       # create a new object
        new_item = CartItem(coffee_id=coffee.id, cart_id=user_cart.id, price=price)
        db.session.add(new_item)
        db.session.commit()

def add_book_to_cart(db, book_name, user_cart, Book, CartItem, price):
    book = Book.query.filter_by(bookName=book_name).first()
    book_item = CartItem.query.filter_by(cart_id=user_cart.id, book_id=book.id).first()
    if book_item:
        book_item.quantity += 1
        db.session.commit()
    else:
        new_item = CartItem(book_id=book.id, cart_id=user_cart.id, price=price)
        db.session.add(new_item)
        db.session.commit()

def add_game_to_cart(db, game_name, user_cart, VideoGame, CartItem, price):
    game = VideoGame.query.filter_by(gameName=game_name).first()
    game_item = CartItem.query.filter_by(cart_id=user_cart.id, game_id=game.id).first()
    if game_item:
        game_item.quantity += 1
        db.session.commit()
    else:
        new_item = CartItem(game_id=game.id, cart_id=user_cart.id, price=price)
        db.session.add(new_item)
        db.session.commit()
