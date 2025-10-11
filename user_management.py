'''import json
import os

USERS_FILE = "users.json"

# Load users from JSON file (Improved with error handling)

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Handle the error if the file is empty or corrupted
        print("Warning: users.json is corrupted or empty. Starting fresh.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while loading users: {e}")
        return {}



# Save users to JSON file

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


# Register a new user

def register_user():
    users = load_users()
    username = input("Enter new username: ")
    if username in users:
        print(f"User '{username}' already exists!")
        return None
    password = input("Enter password: ")
    
    # Store user data with an empty 'progress' dictionary for other modules
    users[username] = {"password": password, "progress": {}}
    save_users(users)
    print(f"User '{username}' registered successfully!")
    return username


# Login user

def login_user():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Invalid username or password!")
        return None


# Run module directly for testing

if __name__ == "__main__":
    print("\n----- User Authentication Module Test -----")
    print("1. Register\n2. Login")
    choice = input("Enter choice (1/2): ")
    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    else:
        print("Invalid choice.")'''






'''import json
import os

USERS_FILE = "users.json"

# Load users from JSON file

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

# Save users to JSON file

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Register a new user

def register_user():
    users = load_users()
    username = input("Enter new username: ")
    if username in users:
        print(" User already exists!")
        return None
    password = input("Enter password: ").strip()
    users[username] = {"password": password, "progress": {}}
    save_users(users)
    print("User registered successfully!")
    return username

# Login user

def login_user():
    users = load_users()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in users and users[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Invalid username or password!")
        return None'''




from database import load_data, save_data

def register_user(username, password):
    data = load_data()
    if username in data["users"]:
        return False, "User already exists!"
    data["users"][username] = {"password": password}
    save_data(data)
    return True, "Registration successful!"

def login_user(username, password):
    data = load_data()
    user = data["users"].get(username)
    if not user:
        return False, "User not found!"
    if user["password"] != password:
        return False, "Incorrect password!"
    return True, "Login successful!"
