# 2⃣ Largest of Three 
# Accept three numbers from the user and print the largest number. 
# (Do not use built-in max function.) 

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a >=b and a>=c:
    print('Largest number is ',a)

elif b >= c and b >= a:
    print('Largest number is ',b)

else:
    print('Largest number is ',c)

