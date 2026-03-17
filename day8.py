# Overview:
# ● Reading and writing files (open(), read(), write())
# ● Handling file exceptions (try-except)
# 📖 Learning Resources:
# ● Python File Handling (W3Schools)
# 📌 Tasks:
# ✅ Create a program that writes user input to a text file
# ✅ Read and print the contents of a file


try:
    user_input = input("Enter some text to write to the file: ")
    with open("user_input.txt", "w") as file:
        file.write(user_input)
    print("Text written to user_input.txt successfully.")
    
    with open("user_input.txt", "r") as file:
        content = file.read()
    print("Contents of the file:")
    print(content)
except Exception as e:
    print(f"An error occurred: {e}")