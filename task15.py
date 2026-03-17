# 5⃣ Student Marks Analyzer 
# Store marks of 5 subjects in a list. 
# Print: 
# ● Total 
# ● Average 
# ● Result (Pass if average ≥ 50, else Fail) 

mark = []

sub1 = int(input('Physics: '))
mark.append(sub1)

sub2 = int(input('Chemistry: '))
mark.append(sub2)

sub3 = int(input('Mathematics: '))
mark.append(sub3)

sub4 = int(input('English: '))
mark.append(sub4)

sub5 = int(input('Biology: '))
mark.append(sub5)

total = sum(mark)
average = total / 5

print('Mark list: ',mark)
print('Total mark:' ,total)
print('Average mark: ',average)

if average >= 50:
    print('Pass')

else:
    print('Fail')


