# 3⃣ Secure Login 
# Create User class: 
# ● Public username 
# ● Private password 
# ● 3 login attempts limit 
# ● Password change with validation 
# Methods / Concepts to Use: 
# ● Encapsulation 
# ● Instance methods 
# ● Conditional logic 
# ● Counter variable 

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__attempts = 0
        self.__max_attempts = 3

    def login(self,password):
        if self.__attempts >= self.__max_attempts:
            print("Account locked ! Too many failed attempts")
            
        elif password == self.__password:
            print("Login Successful")
            self.attempts = 0
        else:
            self.__attempts += 1
            x = self.__max_attempts - self.__attempts
            print(f"Incorrect Password yor balance attempts : {x}")

    def change_password(self, old_password, new_password):
        if old_password != self.__password:
            print("Old password is Incorrect")

        elif len(new_password) < 6:
            print("New Password must be 6 characters")
            return
        
        self.__password == new_password
        print("Password Changed Successfully")

user1 = User("Neethu","neethu@")

user1.login("wrong")
user1.login("passwo")
user1.login("neethh")

user1.login("neethu@")

user1.change_password("neethu@","newpass")