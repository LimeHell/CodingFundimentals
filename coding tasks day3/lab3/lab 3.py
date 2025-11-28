def ShowMM():
    print("main menu")
    print("what task would you like to see")
    print("1. squares")
    print("2. Factorial")
    print("3. Invest")
    print("4. Between limites")
    print("x. exit")
    
def Task1():
    ## Task 1 Squares
    for i in range(1,100):
        isq = i**2
        print(isq)
        if isq >= 2000:
            break

    print("---------------")
    ShowMM()

def Task2():
    ## Task 2 Factorial
    while True:
        try:
            number = int(input("GIVE ME NUMBER FATHER: "))
            break
        except:
            print("THAT IS NOT A NUMBER FATHER PLEASE BE HONEST WITH ME")


    result = 1
    for i in range(1,number+1):
        result = result * i
    print(result)

    print("---------------")
    ShowMM()

def Task3():
    ## Task 3 investment
    while True:
        try:
            Bank = int(input("Enter current cash: "))
            target = int(input("Enter target cash: "))
            intrest = int(input("Enter yearly intreset: "))
            break
        except:
            print("try again son")
    years = 0

    while Bank < target:
        Bank += (Bank * (intrest/100))
        years += 1
        
    print(years)

    print("---------------")
    ShowMM()

def Task4():
    ## Task 4 Input integer between two limits
    min = 1
    max = 100
    lives = 3

    while True:
        guess = int(input("enter first guess"))
        if guess >= 1 and guess <= 100:
            print(" you did it, now leave please")
            break
        else:
            lives -= 1
            print("try again bud, you just lost a life")
            print(f"you now have {lives} lives left")
        if lives == 0:
            print("your too bad buckaroo, you lost")
            break
    print("---------------")
    ShowMM()

def Task5():
    WordInput = input("Enter a word")
    vowels = 0
    vowellist = ["a", "e", "i", "o", "u"]
    for i in WordInput:
        if i.lower() in vowellist:
            vowels += 1
    print(f"word has {vowels} vowels")

ShowMM()
while True:
    mmselect = input("Please select an option")
    if mmselect == "1":
        Task1()
    elif mmselect == "2":
        Task2()
    elif mmselect == "3":
        Task3()
    elif mmselect == "4":
        Task4()
    elif mmselect == "x":
        break
    else:
        print("invalid input")