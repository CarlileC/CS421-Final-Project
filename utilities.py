from markupsafe import Markup
import random

def passwordCheck(password:str, confirmPassword:str) -> list:    
        upper = False
        lower = False
        number = password[-1].isdigit()
        length = len(password) >= 8
        passwordMatch = False
        
        for i in password:
            if i.isupper() == True:
                upper = True
            elif i.islower() == True:
                lower = True

        if password == confirmPassword:
            passwordMatch = True
    
        message = "<p>Oh no! Looks like you had issues with your password! <br><br> Here are the requirements you failed:<p> <ul class='errorMessage'>"
        
        
        
        if password != confirmPassword:
            passwordMatch = False
    
        if(not upper):
            message += "<li>You did not use an upper case letter</li>"
        if(not lower):
            message += "<li>You did not use a lower case letter</li>"
        if(not number):
            message += "<li>You did not use a number at the end</li>"
        if(not length):
            message += "<li>Your password is less than 8 characters</li>"
        if not passwordMatch:
            message += "<li>Your passwords did not match</li>"
        
        
        if(upper and lower and number and length):
            return [True]
        else:
            message += "</ul>"
            returnMessage = Markup(message)
            return [False, returnMessage]
        
def add_coffee_to_cart(db, coffee_name, user_cart, Coffee, CartItem, price):
    coffee = Coffee.query.filter_by(coffeeName=coffee_name).first()
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

def order_number_generator(Order):
    new_id = random.randint(1, 10000000000)
    Order.order_number = new_id
    return new_id

def add_new_comment(db, summary_form_data, comment_form_data, user, coffee_id, Comment):
    comment = Comment(summary=summary_form_data, comment=comment_form_data, coffee_id=coffee_id, user=user)
    db.session.add(comment)
    db.session.commit()
    db.session.flush()