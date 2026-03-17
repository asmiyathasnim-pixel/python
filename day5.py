# Overview:
# ● Defining and calling functions
# ● Parameters and return values
# ● Function scope (global, local)
# 📖 Learning Resources:
# ● Python Functions (W3Schools)
# 📌 Tasks:
# ✅ Write a function that takes two numbers and returns their sum


def add_numbers(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum_result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {sum_result}")

# ✅ Create a function that checks if a number is even or odd

num = int(input("Enter a number to check if it's even or odd: "))
if is_even(num):
    print(f"{num} is even.")    
else:
    print(f"{num} is odd.")


