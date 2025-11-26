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
p3 = Person("still a", "now am i?")

for i in People:
    i.middlename = "Gooza"
    print(i.firstname, i.middlename, i.lastname)

Person.middlename = "Geeeza"
for i in People:
    print(i)
    print(i.firstname, i.middlename, i.lastname)

Jobs = []
class Job:
    def __init__(self, JobName, Salery, QualificationReq, PossibleEmployees, Description):
        class JobName(Person):
            pass
        self.Salery = Salery
        self.QualificationReq = QualificationReq
        self.PossibleEmployees = PossibleEmployees
        self.Description = Description
        Jobs.append(self)

Devops = Job("£5", "Jawline", 7, "Tell people how to do their jobs well")

        
    
    