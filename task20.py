# �
# �
# Student Data Formatter 
# Take input: 
# ● Name 
# ● Age 
# ● 3 Skills 
# Store them properly and display output like: 
# Rahul (Age: 21) knows Python, SQL, and Excel. 
# Also convert the stored data into structured data format and print 
# it

a = []
name = input('Enter your name: ')
age = int(input('Enter your age: '))
skill = input('Enter your 3 skills: ')

a.append(name)
a.append(age)
a.append(skill)

print(f'{name} (Age : {age}) knows {skill}')

data = {
    "name": name,
    "age": age,
    "skills": skill,
}

print("Structured Data:")
print(data)


