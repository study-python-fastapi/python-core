user1 = {"username": "Tom", "password": "password123"}
user2 = {"username": "Ema", "password": "qwertyqwerty"}
list_of_users = [user1, user2]

for user in list_of_users:
    if user["password"] == "password123":
        print("You're in system")
    else:
        print("password is wrong")

