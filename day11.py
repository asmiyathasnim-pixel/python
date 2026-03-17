# Overview:
# ● Introduction to APIs & requests module
# ● Fetching data from a free API
# (https://jsonplaceholder.typicode.com/users)
# 📖 Learning Resources:
# ● Python Requests Module (Real Python)
# 📌 Tasks:

# ✅ Fetch and display a list of users from an API

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code == 200:
    users = response.json()
    print("List of Users:")
    for user in users:
        print(f"Name: {user['name']}, Email: {user['email']}")      
else:
    print("Failed to retrieve data from the API")
    print(f"Status Code: {response.status_code}")

    