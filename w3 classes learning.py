People = []

class Person:
    def __init__(self, firstname, lastname):
        People.append(self)
        self.firstname = firstname
        self.lastname = lastname
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} mogs you btw"
        
p1 = Person("Jude", "Stone")
p2 = Person("not Jude", "Stone")
Person.middlename = "Geeeza"
for i in People:
    print(i)
