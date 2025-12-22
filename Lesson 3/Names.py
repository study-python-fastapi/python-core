user_1 = {
    "user_name": "tester",
    "rule": "admin",
    "account_connection": True
}
user_2 = {
    "user_name": "junior",
    "rule": "user",
    "account_connection": False
}
user_3 = {
    "user_name": "middler",
    "rule": "user",
    "account_connection": True
}

list_of_users = [user_1, user_2, user_3]

for user in list_of_users:
    print(f"Work with usser {user['user_name']}")
    if not user["account_connection"]:
        attemps = 10
        while attemps >= 0:
            if attemps == 0:
                print("You lose")
                break
            else:
                print("Try to connect to user account")
            attemps -= 1
            print("Attemps:", attemps)
    elif user["rule"] == "admin":
        print("Admin user")
    else:
        print("User not found")