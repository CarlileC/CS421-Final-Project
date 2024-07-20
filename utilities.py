from markupsafe import Markup

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