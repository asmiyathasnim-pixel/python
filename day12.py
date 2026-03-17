# Overview:
# ● Using pickle to save user data
# ● Saving and retrieving data using files
# 📖 Learning Resources:
# ● Python Pickle Module (GeeksForGeeks)
# 📌 Tasks:
# ✅ Save a user’s name in a file and display it on program restart

import pickle

def save_name(name):
    with open("user_data.pkl", "wb") as file:
        pickle.dump(name, file)
def load_name():
    try:
        with open("user_data.pkl", "rb") as file:
            name = pickle.load(file)
            return name
    except FileNotFoundError:
        return None
user_name = load_name()
if user_name:
    print(f"Welcome back, {user_name}!")
else:
    user_name = input("Enter your name: ")
    save_name(user_name)
    print(f"Hello, {user_name}! Your name has been saved.")