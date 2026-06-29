# ==========================================
# PROJECT 2 - REGISTER AND LOGIN
# ==========================================
# Version 5
# - Improved registration flow for duplicate usernames and emails.
# - Moved duplicate username and email checks into registration input validation.
# - Registration now asks again immediately when username or email is already taken.
# ==========================================

# ==========================================
# CONSTANTS
# ==========================================
# Message constants for user feedback
INVALID_EMAIL = 'Invalid email format. \nPlease enter a valid email address between 5 and 64 characters.'
EMAIL_TAKEN = 'Email already registered.\nPlease choose a different email.'
INVALID_USERNAME = 'Invalid username. \nUsername must be alphanumeric and between 3 and 20 characters long.'
USERNAME_TAKEN = 'Username already exists.\nPlease choose a different username.'
INVALID_PASSWORD = 'Invalid password. \nPassword must be between 8 and 128 characters long and include both letters and numbers.'
LOGIN_OR_REGISTER = "Do you want to login, register, or exit? (login/register/exit): "
INVALID_CHOICE = "Invalid choice. Please enter 'login', 'register', or 'exit'."
LOGIN = "You have chosen to login.\nPlease enter your username or email and password."
REGISTER = "You have chosen to register.\nPlease enter your username, email, and password."
LOGIN_SUCCESS = "Login successful!\nWelcome, {}!"
LOGIN_FAILED = "Login failed. Please check your username or email and password."
REGISTER_SUCCESS = "Registration successful!\nWelcome, {}!"
EXIT_MESSAGE = "Exiting the program."

# Validation limits for user input
MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 20
MIN_EMAIL_LENGTH = 5
MAX_EMAIL_LENGTH = 64
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 128


# ==========================================
# PROGRAM DATA
# ==========================================
users = []


# ==========================================
# CLASSES
# ==========================================
class UserInput:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


# ==========================================
# FUNCTIONS
# ==========================================
def get_registration_input(prompt, input_type):
    """
    Gets user input for a specific type (username, email, or password) and validates it.

    Args:
        prompt (str): The prompt to display to the user.
        input_type (str): The type of input to validate ("username", "email", or "password").
        
    Returns:
        str: The validated user input.
    """
    while True:
        if input_type == "username":
            user_input = input(prompt).strip()
            username_taken = False

            if not user_input.isalnum() or not (MIN_USERNAME_LENGTH <= len(user_input) <= MAX_USERNAME_LENGTH):
                print(INVALID_USERNAME)
                continue

            for user in users:
                if user.username.lower() == user_input.lower():
                    username_taken = True
                    break

            if username_taken:
                print(USERNAME_TAKEN)
                continue

            return user_input

        elif input_type == "email":
            user_input = input(prompt).strip()
            email_taken = False

            if not (MIN_EMAIL_LENGTH <= len(user_input) <= MAX_EMAIL_LENGTH):
                print(INVALID_EMAIL)
                continue

            if user_input.count('@') != 1 or user_input.startswith('@') or user_input.endswith('@'):
                print(INVALID_EMAIL)
                continue

            local_part, domain = user_input.split('@')

            if len(local_part) < 1 or len(domain) < 3 or '.' not in domain:
                print(INVALID_EMAIL)
                continue

            domain, top_domain = domain.rsplit('.', 1)

            if len(top_domain) < 2 or len(top_domain) > 6 or not top_domain.isalpha():
                print(INVALID_EMAIL)
                continue
                
            for user in users:
                if user.email.lower() == user_input.lower():
                    email_taken = True
                    break

            if email_taken:
                print(EMAIL_TAKEN)
                continue

            return user_input

        elif input_type == "password":
            user_input = input(prompt).strip()

            if not (MIN_PASSWORD_LENGTH <= len(user_input) <= MAX_PASSWORD_LENGTH) or not any(char.isdigit() for char in user_input) or not any(char.isalpha() for char in user_input):
                print(INVALID_PASSWORD)
                continue
                
            return user_input
            
def get_registration_information():
    """
    Gets user information for registration.
    
    Returns:
        tuple: A tuple containing the username, email, and password if all are valid, otherwise None.
    """      
    username = get_registration_input("Enter your username: ", "username")
    email = get_registration_input("Enter your email: ", "email")
    password = get_registration_input("Enter your password: ", "password")
    return username, email, password

def get_login_information():
    """
    Gets user information for login.
    
    Returns:
        tuple: A tuple containing the inputted login_id and password.
    """      
    login_id = input("Enter your username or email: ").strip().lower()
    password = input("Enter your password: ").strip()
    return login_id, password 

def login_options():
    """
    Provides the user with options to either login or register and stores or retrieves validated user information.
    Checks for existing usernames and emails during registration and validates login credentials.
    """
    while True:
        login_or_register = input(LOGIN_OR_REGISTER).strip().lower()

        if login_or_register == "login":
            print(LOGIN)
            login_id, password = get_login_information()
            user_found = False

            for user in users:
                if (user.username.lower() == login_id or user.email.lower() == login_id) and user.password == password:
                    print(LOGIN_SUCCESS.format(user.username))
                    user_found = True
                    break

            if not user_found:
                print(LOGIN_FAILED)
                continue

        elif login_or_register == "register":
            print(REGISTER)
            username, email, password = get_registration_information()
            new_user = UserInput(username, email, password)
            users.append(new_user)
            print(REGISTER_SUCCESS.format(username))

        elif login_or_register == "exit":
            print(EXIT_MESSAGE)
            break

        else:
            print(INVALID_CHOICE)


# ==========================================
# MAIN PROGRAM
# ==========================================
login_options()