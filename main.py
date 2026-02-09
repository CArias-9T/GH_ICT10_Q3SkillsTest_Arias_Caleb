# nested if-statment

from pyscript import display, document

def account_verify(e):
    document.getElementById('output').innerHTML = '' # resets value
    
    username = document.getElementById('input1').value

    password = document.getElementById('input2').value

    # one nested if statement

    if len(password) >= 10 and len(username) >= 7: # primary check, if the username's length is 7 or more and if the password's length is 10 or more
        if not password.isalpha(): # secondary check for the password, checks if it contains solely letters
            if password.isdigit(): # final check for the password, checks if it contains solely numbers
                display(f"Your username is eligible. Your password must contain both letters and numbers. Please add letters.", target="output")
    
            else: # if the second and third check are false, sign in
                display(f"You are signed up, {username}! Welcome!", target="output")

        elif password.isalpha():
            display(f"Your username is eligible. Your password must contain both letters and numbers. Please add numbers.", target="output")

    elif not len(password) >= 10 and len(username) >= 7:
            display(f"Your username is eligible. Your password must be 10 characters or more.", target="output")
    
    elif not len(password) >= 10 and not len(username) >= 7:
            display(f"Your username must be 7 characters or more. Your password must be 10 characters or more.", target="output")
    
    elif len(password) >= 10 and not len(username) >= 7:
            display(f"Your username must be 7 characters or more.", target="output")

    



