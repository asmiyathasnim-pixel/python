# 3⃣ Sum Until Zero 
# Keep asking the user to enter numbers. 
# Stop only when the user enters 0. 
# Finally print the total sum of all entered numbers. 

num = 0

while True:
    a = int(input('Enter a number:'))
    num += a
    if a == 0:
        break

print('Total sum: ',num)
