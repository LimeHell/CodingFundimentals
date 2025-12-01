def menugenerator(title, options):
    count = 1
    print(title)
    for i in options:
        print(f"{count}. {i}")
        count += 1
    input("What options would you like to select: ")
        
options = ["eat joe", "eat dees", "eat bruh"]
menugenerator("Menu", options)