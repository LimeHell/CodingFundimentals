import inspect
# this is big ol file so i can learn what classes do and how far i can strech them
#Array elemnt and property printer
class Controller:
    def __init__(self, Array, Properties):
        self.Array = Array
        self.Properties = Properties
    
    def PrintEach(self):
        for Element in self.Array:
            print(Element)

    def WeakPrintProperties(self): 
        for Element in self.Array:
            ElementProperties = []
            for Property in self.Properties:
                try:
                    ElementProperties.append(getattr(Element, Property))
                except:
                    break
            print(" ".join(ElementProperties))
            
    def StrongPrintProperties(self): 
        for Element in self.Array:
            ElementProperties = []
            for Property in self.Properties:
                    ElementProperties.append(getattr(Element, Property))
            print(" ".join(ElementProperties))        
    
# Have an array for all people
People = []
PeopleProperties = ["FirstName","MiddleName", "LastName"]
PC = Controller(People, PeopleProperties)
Judes = []
JC = Controller(Judes, [])

#Define person
class Person:
    def __init__(self, FirstName, LastName):
        People.append(self)
        self.FirstName = FirstName
        self.LastName = LastName
        if FirstName == "Jude":
            Judes.append(self)
    
    def __str__(self):
        return f"{self.FirstName} {self.LastName} mogs you btw"

#Some sample people 
p1 = Person("Jude", "Cool")
p2 = Person("Jude", "Epic")
p3 = Person("jawline", "enjoyer")

#adding a middle name to the Judes
for Jude in Judes:
    Jude.MiddleName = "Gooza"
    
#have a look
PC.WeakPrintProperties()

# add a middle name property permenatly to the class
Person.MiddleName = "Geeeza"
#New person for control
p4 = Person("Still a", "yeah mate")

#have another look
PC.PrintEach()
PC.WeakPrintProperties()

# lets make the job class to make more classes
Jobs = []
class Job:
    def __init__(self, JobName, Salery, QualificationReq, PossibleEmployees, Description):
        class JobName(Person):
            def __init__(self, FirstName, LastName):
                super().__init__(FirstName, LastName)
                if len(inspect.getmembers(JobName)) > QualificationReq:
                    del self
            pass
        self.Salery = Salery
        self.QualificationReq = QualificationReq
        self.PossibleEmployees = PossibleEmployees
        self.Description = Description
        Jobs.append(self)
    def class

DevOpsJob = Job("DevOps", "£5", "Jawline", 7, "Tell people how to do their jobs well")