# 1⃣ Number Nature 
# Write a program that takes a number from the user and prints: 
# ● “Divisible by 3 only” 
# ● “Divisible by 5 only” 
# ● “Divisible by both 3 and 5” 
# ● “Not divisible by 3 or 5” 


a = int(input("enter a number:"))

if a % 3 ==0 and a % 5 ==0:
    print('Divisible by both 3 & 5')

elif a % 3 ==0:
    print('Divisible by 3')

elif a % 5 ==0:
    print('Divisible by 5')

else:
    print('Not divisible by 3 0r 5')


