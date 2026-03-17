# Overview:
# ● Lists & dictionaries
# ● List methods (append(), pop(), sort(), reverse())
# ● Dictionaries { key: value } syntax
# ● Dictionary methods (keys(), values(), items())
# 📖 Learning Resources:
# ● Python Lists (W3Schools)
# ● Python Dictionaries (GeeksForGeeks)
# 📌 Tasks:
# ✅ Create a list of your favorite movies and print them


favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
print("Favorite Movies:")
for movie in favorite_movies:
    print(movie)
person = {"name": "asmiya", "age": 18, "city": "New York"}

# ✅ Define a dictionary with properties name, age, city

print("\nPerson Dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")


    