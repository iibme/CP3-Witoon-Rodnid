user = 0
password = 0
while user != "iibme" or password != "2808":
    user = input("Username")
    password = input("Password")
    if user == "iibme" and password == "2808":
        print("Done!!")
    else:
        print("Username or password is not correct please try again")

