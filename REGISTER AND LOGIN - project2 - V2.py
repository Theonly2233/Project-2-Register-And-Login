# ==========================================
# PROJECT 2 - REGISTER AND LOGIN
# ==========================================
# Version 2
# - Combined "get_information_login" and "get_information_register" functions.
# - Nested get_input for better readability.
# - Fixed recursive code.
# - Fixed the "for" loop to ensure it scans each object, not just one.
# ==========================================

user_inputs = []

username = ''
email = ''
password = ''
# ======================================================================
# FUNCTIONS
# ======================================================================
class UserInput:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
            
def get_information():
    def get_input(prompt, input_type):
        while True:
            if input_type == "username":
                user_input = input(prompt).strip()
                if not user_input.isalnum() or len(user_input) < 3:
                    print('Invalid username. \nUsername must be alphanumeric and at least 3 characters long.')
                else:
                    return user_input

            elif input_type == "email":
                user_input = input(prompt).strip()
                if "@" not in user_input or "." not in user_input:
                    print('Invalid email. \nEmail must contain "@" and "." characters.')
                else:
                    return user_input

            elif input_type == "password":
                user_input = input(prompt).strip()
                if not len(user_input) >= 8 or not any(char.isdigit() for char in user_input) or not any(char.isalpha() for char in user_input):
                    print('Invalid password. \nPassword must be at least 8 characters long and include both letters and numbers.')
                else:
                    return user_input
                
    username = get_input("Enter your username: ", "username")
    email = get_input("Enter your email: ", "email")
    password = get_input("Enter your password: ", "password")
    return username, email, password

def login_options():
    while True:
        login_or_register = input("Do you want to login or register? (login/register): ").lower()

        if login_or_register == "login":
            print("You have chosen to login.\nPlease enter your username, email, and password.")
            username, email, password = get_information()
            user_found = False
            for user in user_inputs:
                if user.username == username and user.email == email and user.password == password:
                    print("Login successful!\nWelcome, {}!".format(user.username))
                    user_found = True
                    break
            if not user_found:
                print("Login failed. Please check your username/email and password.")
                continue

        elif login_or_register == "register":
            print("You have chosen to register.")
            username, email, password = get_information()
            new_user = UserInput(username, email, password)
            user_inputs.append(new_user)
            print("Registration successful!\nWelcome, {}!".format(username))

        else:
            print("Invalid choice. Please enter 'login' or 'register'.")


# ======================================================================
# MAIN PROGRAM
# ======================================================================
login_options()
