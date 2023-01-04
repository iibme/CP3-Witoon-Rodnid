user = input("username")
password = input("pass word")
if user == "iibme" and password == "28081999":
    print("------Welcome To My Cafe------")
    print("1. Americano   45    THB")
    print("2. Espresso    50    THB")
    print("3. Latte       55    THB")
    print("4. Cappuccino  55    THB")
    print("5. Mocca       60    THB")
    userSelected =  input("What would you like to order?")
    Numberproduct = int(input("How many cups do you get?"))
    if userSelected == "Americano" :
        print("Americano---",Numberproduct,"---",45*Numberproduct,"THB")
    elif userSelected == "Espresso" :
        print("Esoresso---",Numberproduct,"---",50*Numberproduct,"THB")
    elif userSelected == "Latte" :
        print("Latte---",Numberproduct,"---",55*Numberproduct,"THB")
    elif userSelected == "Cappuccino" :
        print("Cappuccino---",Numberproduct,"---",55*Numberproduct,"THB")
    elif userSelected == "Mocca" :
        print("Mocca---",Numberproduct,"---",60*Numberproduct,"THB")
    print(" THANK YOU ENJOY YOUR DRINK ")
else:
    print("Username and Password incorrectly Please try again")









