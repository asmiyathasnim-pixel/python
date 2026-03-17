# 4⃣ Multiplication Table Generator 
# Ask the user for a number and print its multiplication table up to 
# 12.

a=int(input("enter number : "))

for x in range(1,13):
    print(f'{x} x {a} = {x * a}')
