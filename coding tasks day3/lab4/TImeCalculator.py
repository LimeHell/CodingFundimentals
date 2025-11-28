def ShowMM():
    print("Time Calculator")
    print("1. Add 2 times (DD:HH:MM)")
    print("2. Find the diffrence between 2 Times (DD:HH:MM)")
    print("3. Convert (DD:HH:MM) to Hours")
    print("4. Convert (DD:HH:MM) to Miniutes")
    print("5. Convert Minuites to Time (DD:HH:MM)")
    print("6. Convert Hours to Time (DD:HH:MM)")
    print("7. Convert Days to TIme (DD:HH:MM)")
    print("8. Exit")

def validatetime(Time):
    Split = Time.split(":")
    for i in Split:
            try:
                int(i)
            except:
                return False
    return True
    
def TwoTimes(funcnum):
    while True:
        Time1 = input("Enter the first Time (DD:HH:MM): ")
        Time2 = input("Enter the second Time (DD:HH:MM): ")
        validin = validatetime(Time1)
        validin = validatetime(Time2)
        if validin:
            break
        else: 
            print("Invalid time buckaroo")
    
    
ShowMM()
while True:
    MMSelection = input("What would you like to do?: ")
    if MMSelection == "1":
        TwoTimes(1)
    elif MMSelection == "2":
        print("ea sports")
    elif MMSelection == "3":
        print("ea sports")
    elif MMSelection == "4":
        print("ea sports")
    elif MMSelection == "5":
        print("ea sports")
    elif MMSelection == "6":
        print("ea sports")
    elif MMSelection == "7":
        print("ea sports")
    elif MMSelection == "8":
        print("ea sports")
    else:
        print("Invalid input")
    