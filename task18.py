# 8⃣ Calculator Menu 
# Create a program that asks the user to choose an operation: 
# ● Add 
# ● Subtract 
# ● Multiply 
# ● Divide 
# Take two numbers and perform the selected operation. 

num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2st Number: '))
optr = input('Select operator (+, -, *, /): ')

if optr == '+':
    print(num1 + num2)

elif optr == '-':
    print(num1 - num2)

elif optr == '*':
    print(num1 * num2)

else:
    print(num1 / num2)

