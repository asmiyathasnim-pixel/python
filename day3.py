# Overview:
# ● Arithmetic (+, -, *, %, /), Comparison (==, >=, <=, !=), and Logical Operators (and,
# or, not)
# ● if, elif, else conditional statements
# ● Ternary operator (value_if_true if condition else value_if_false)
# 📖 Learning Resources:
# ● Python Operators (W3Schools)
# ● Python Conditions (GeeksForGeeks)
# 📌 Tasks:
# ✅ Write a program to check if a number is positive, negative, or zero


number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# ✅ Create a login system with hardcoded username/password

username = "asmiya"
password = "12345"
input_username = input("Enter username: ")
input_password = input("Enter password: ")
if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Login failed. Incorrect username or password.")