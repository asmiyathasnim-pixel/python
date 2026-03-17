# 9⃣ Safe Number Input 
# Ask the user to enter a number and print its square. 
# If the user enters invalid input, display: 
# “Invalid input. Please enter numbers only.” 


try:
    numbr = int(input('enter a number: '))
    x = numbr * numbr
    print(x)
except:
    print('Invalid input. Please enter a number,')

