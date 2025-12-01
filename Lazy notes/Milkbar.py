def MilkShakeBar():
    while True:
        try:
            Budget = int(input("What's your budget?: "))
            break
        except:
            print("invalid")
            
    menu = ["Choclate D: £15", "Plum and Rasin: £20", "Strawberry Martni: £12"]
    prices = [15, 20, 12]
    
    print("Milkshake Bar")
    print(f"1. {menu[0]}")
    print(f"2. {menu[1]}")
    print(f"3. {menu[2]}")
    
    print("Q. Exit")
    
    while True:
        Choice = input("What is your selection: ")
        if Choice == "1" and Budget >= prices[0] :
            Budget -= prices[0]
            print(f"Here you go son heres a {menu[0]}")
        elif Choice == "2" and Budget >= prices[1]:
            Budget -= prices[1]
            print(f"Here you go son heres a {menu[1]}")
        elif Choice == "3" and Budget >= prices[2]:
            Budget -= prices[2]
            print(f"Here you go son heres a {menu[2]}")
        elif Choice.lower() == "q":
            print("Goodbye")
            break
        elif Choice == "1" or Choice == "2" or Choice == "3":
            print("Get out of my shop you milkshake-aholic")
            break
        else:
            print("Invalid Option")
  
menu = ["Choclate D: £15", "Plum and Rasin: £20", "Strawberry Martni: £12"]      

MilkShakeBar()