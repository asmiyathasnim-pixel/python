# Biggest Number Finder 
# Write a program that takes some numbers from the user and shows which number is the 
# biggest. 
# If two or more numbers are the same, show that clearly

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

if num1 > num2:
    print(num1,'is greater') 
elif num1 == num2:
    print(f"{num1} and {num2} are equal")
else:
    print(num2,'is greater')