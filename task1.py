# 1.User Introduction 
# Write a program that asks for a person’s details and prints a short introduction about that 
# person. 
# The program should also decide if the person is allowed to sign up based on age.


name = input('Enter your Name:')
age = int(input('Enter your Age:'))
city = input('Enter your  City:')

print(f'My name is {name}. I am {age} years old, iam from {city}.')

if age >= 18:
    print('You are able to signup.')
    

else:
    print('You are not not able to signup.Your age must be 18 or above')
