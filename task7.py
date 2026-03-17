# Marks Comparison

group1 = {
     int(input('Enter the mark: ')),
     int(input('Enter the mark: ')),
     int(input('Enter the mark: ')),
     int(input('Enter the mark: ')),
}

print('Enter group 2 mark: ')

group2 = {
     int(input('Enter the mark: ')),
     int(input('Enter the mark: ')),
     int(input('Enter the mark: ')),
     int(input('Enter the mark: ')),
}

same_mark= []
different_mark = []

for mark in group1 :
    if mark in group2:
         same_mark.append(mark)
    else:
         different_mark.append(mark)


print("group one mark :",group1)
print("group two mark :",group2)
print("same mark :", same_mark)
print("different mark :",different_mark)