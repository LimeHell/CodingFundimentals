def SearchByAuthor():
    Search = input("What Author do you want?: ")
    discography = Library.get(Search, "This authour is not apart of the library")
    print(", ".join(discography))

def SearchByBook():
    Search = input("What Book do you want?: ")
    for k, v in Library.values:
        if v == Search:
            print(f"{v} was written by {k}") 
            break
    print("sorry book is not present")

def AddAnAuthor():
    Request = input("Please enter the name of the author you wish to add")
    BookRequest = input("Please add any books they have written sperated by a comma and space (eg 1, 2, 3,)")
    try:
        Library[Request] = ", ".split(BookRequest)
        print("Author has been sucsessfully added")#
    except:
        print("Syntax Error")

def AddABook():
    Request = input("Please enter the name of the book's author")
    BookRequest = input("Please add any books you want to add sperated by a comma and space (eg 1, 2, 3,)")
    try:
        Library[Request] = ", ".split(BookRequest)
        print("Book(s) has been sucsessfully added")#
    except:
        print("Syntax Error")
        
Library = {"James": ["Gaint Peach","Gainter peach","Gaintest peach"], "Moby": ["Dick", "Richard", "Rich"], "Decartes": ["Meditations1", "Meditations2", "Meditations3"]}

print("Main Menu")
print("1. Search by author")
print("2. Search by book")
print("3. Add an author")
print("4. Add a book")
print("5. Exit")
MMSelection =input("Select option: ")

while True:
    if MMSelection == 1:
        SearchByAuthor()
    elif MMSelection == 2:
        SearchByBook()
    elif MMSelection == 3:
        AddAnAuthor()
    elif MMSelection == 4:
        AddABook()
    elif MMSelection == 5:
        break
    else:
        print("invalid option")
        

