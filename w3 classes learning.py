class Controller:
    def __init__(self, array, properties):
        self.array = array
        self.properties = properties
    
    def PrintEach(self):
        for element in self.array:
            print(element)

    def PrintProperties(self):
        for element in self.array:
            ElementProperties = []
            for property in self.properties:
                ElementProperties.append(element.property)
            print(ElementProperties.join(" "))

# Have an array for all people
People = []
PeopleProperties = ["firstname", "lastname", "middlename"]
PC = Controller(People, PeopleProperties)
Judes = []
JC = Controller(Judes)

#Define person
class Person:
    def __init__(self, firstname, lastname):
        People.append(self)
        self.firstname = firstname
        self.lastname = lastname
        if firstname == "Jude":
            Judes.append(self)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} mogs you btw"

#Some sample people 
p1 = Person("Jude", "Stone")
p2 = Person("Jude", "Epic")
p3 = Person("jawline", "enjoyer")

#adding a middle name to the Judes
for i in Judes:
    i.middlename = "Gooza"
for i in People:
    print(i.firstname, i.middlename, i.lastname)

# add a middle name for 
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

Devops = Job("DevOps", "£5", "Jawline", 7, "Tell people how to do their jobs well")

        
    
    