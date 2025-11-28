def Convert():
    
    print("------------")
    print("Enter current unit")
    print("1. Pounds")
    print("2. Kilograms")
    
    while True:
        weight_unit_selection = input("Enter selection: ")
        
        if weight_unit_selection == "1":
            Units = "lb"
            break
        
        elif weight_unit_selection == "2":
            Units = "KG"
            break
        
        else:
            print("invalid input")
            print("------------")
    
    while True:
        
        try:
            print("------------")
            weight_selection = int(input("Enter Amount: "))
            break
        
        except:
            print("invalid input")
            
    print(f"you have inputted {weight_selection} {Units}")
    print("------------")
    
    print("Enter desired unit")
    print("1. Pounds")
    print("2. Kilograms")
    
    while True:
        out_weight_unit_selection = input("Enter selection: ")
        
        if out_weight_unit_selection == "1" and Units != "lb":
            out_units = "lb"
            break
        
        elif out_weight_unit_selection == "2" and Units != "KG":
            out_units = "KG"
            break  
        
        else:
            print("invalid input")
            print("------------")
    
    if Units == "KG":
        in_ratio = 1
        
    if Units == "lb":
        in_ratio = 2.2
        
    if out_units == "KG":
        out_ratio = 1
        
    if out_units== "lb":
        out_ratio = 2.2
        
    output = (weight_selection / in_ratio) * out_ratio
    print("------------")
    print(f"{weight_selection} {Units} is converted to {output} {out_units}")
    print("------------")
    print("Menu")
    print("1. Convert Weight")
    print("2. Exit")
    
    
print("Menu")
print("1. Convert Weight")
print("2. Exit")

while True:
    selection = input("Enter selection: ")
    
    if selection == "1":
        Convert()
    elif selection == "2":
        break
    
    else:
        print("invalid input")
        print("------------")


