# . Student Result 
# Write a program that takes marks of a student and prints the total, average, and final result. 


subject1 = int(input('Enter the mark: '))
subject2 = int(input('Enter the mark: '))
subject3 = int(input('Enter the mark: '))
subject4 = int(input('Enter the mark: '))

total = (subject1 + subject2 + subject3 + subject4)

average = total/4

if total <=40:
    result = "Fail"

else:
    result = "Pass"


print(f'students result')
print(f'The total marks = {total}')
print(f'The average mark = {average}')
print(result)

