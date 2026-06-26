# ==========================================
# PROJECT 2 - REGISTER AND LOGIN
# ==========================================
# Version 1
# - Initial version of the project.
# ==========================================

user_inputs = []

# ======================================================================
# FUNCTIONS
# ======================================================================
class UserInput:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

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
            
def get_information_login():
    username = get_input("Enter your username: ", "username")
    email = get_input("Enter your email: ", "email")
    password = get_input("Enter your password: ", "password")

    for user in user_inputs:
        if user.username == username and user.email == email and user.password == password:
            print("Login successful!\nWelcome, {}!".format(user.username))
            login_options()
            return
        else:
            print("Login failed. Please check your username/email and password.")
            login_options()
            return

def get_information_register():
    username = get_input("Enter your username: ", "username")
    email = get_input("Enter your email: ", "email")
    password = get_input("Enter your password: ", "password")

    new_user = UserInput(username, email, password)
    user_inputs.append(new_user)
    print("Registration successful!\nWelcome, {}!".format(username))

def login_options():
    while True:
        login_options = input("Do you want to login or register? (login/register): ").lower()

        if login_options == "login":
            print("You have chosen to login.\nPlease enter your username, email, and password.")
            get_information_login()

        elif login_options == "register":
            print("You have chosen to register.")
            get_information_register()

        else:
            print("Invalid choice. Please enter 'login' or 'register'.")


# ======================================================================
# MAIN PROGRAM
# ======================================================================
login_options()
