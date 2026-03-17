# 6⃣ Countdown System 
# Ask the user to enter a starting number. 
# Print countdown till 1 and finally print “Blast Off!”


def countdown(n):
  if n <= 0:
    print("Blast off!")
  else:
    print(n)
    countdown(n -1)

countdown(int(input('Enter a number: ')))


