menulist = []
def showbill():
    total = 0
    print("------My Food------")
    for number in range(len(menulist)):
        print(menulist[number],   "THB")
        total += int(menulist[number][1])
        print("Total",total,    "THB")
while True:
    menuname = input("please enter your menu :")
    if menuname.lower() == "exit":
        break
    else:
        menuprice = input("price :")
        menulist.append([menuname,menuprice])
showbill()