# Overview:
# ● Exception Handling (try, except, finally)
# ● Raising custom exceptions (raise)
# 📖 Learning Resources:
# ● Python Exception Handling (W3Schools)
# 📌 Tasks:


# ✅ Write a program that catches ZeroDivisionError

class AgeValidationError(Exception):
    """Custom exception for invalid age."""
    pass
def validate_age(age):
    if age < 0 or age > 120:
        raise AgeValidationError("Age must be between 0 and 120.")
try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# ✅ Create a custom exception for age validation

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print(f"Your age is: {age}")
except AgeValidationError as ave:
    print(f"Age validation error: {ave}")
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")

    