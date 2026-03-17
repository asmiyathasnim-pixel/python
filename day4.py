# Overview:
# ● for, while, break, continue
# ● Iterating over sequences (range(), list, tuple, dict)
# 📖 Learning Resources:
# ● Python Loops (W3Schools)
# 📌 Tasks:
# ✅ Print numbers 1 to 10 using a loop
# ✅ Write a program to find the sum of numbers from 1 to N


N = int(input("Enter a positive integer N: "))
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)
sum_N = 0
for i in range(1, N + 1):
    sum_N += i
print(f"The sum of numbers from 1 to {N} is: {sum_N}")

