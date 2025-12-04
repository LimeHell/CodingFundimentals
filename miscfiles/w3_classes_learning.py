"""My testing for learning about classes

Returns:
    None: doesn't return anything at all
"""
import inspect
# this is big ol file so i can learn what classes do and how far i can stretch them
# Array element and property printer
class Controller:
    def __init__(self, array, properties):
        """_summary_

        Args:
            array (_type_): _description_
            properties (_type_): _description_
        """
        self.array = array
        self.properties = properties

    def print_each(self):
        for element in self.array:
            print(element)

    def weak_print_properties(self):
        for element in self.array:
            element_properties = []
            for property in self.properties:
                try:
                    element_properties.append(getattr(element, property))
                except:
                    break
            print(" ".join(element_properties))

    def strong_print_properties(self):
        for element in self.array:
            element_properties = []
            for property in self.properties:
                element_properties.append(getattr(element, property))
            print(" ".join(element_properties))

# Have an array for all people
people = []
people_properties = ["FirstName","MiddleName", "LastName"]
people_controller = controller(people, people_properties)
judes = []
jude_controller = controller(judes, [])


# Define person
class Person:
    def __init__(self, first_name, last_name):
        people.append(self)
        self.first_name = first_name
        self.last_name = last_name
        if first_name == "Jude":
            judes.append(self)

    def __str__(self):
        return f"{self.first_name} {self.last_name} mogs you btw"

#Some sample people
p1 = Person("Jude", "Cool")
p2 = Person("Jude", "Epic")
p3 = Person("jawline", "enjoyer")

# adding a middle name to the Jude's
for jude in judes:
    jude.middle_name = "Gooza"

#have a look
people_controller.weak_print_properties()

# add a middle name property permenatly to the class
Person.MiddleName = "Geeeza"
# New person for control
p4 = Person("Still a", "yeah mate")

# have another look
people_controller.print_each()
people_controller.weak_print_properties()

# lets make the job class to make more classes
Jobs = []


class Job:
    def __init__(
        self, job_name, salary, qualification_req, possible_employees, description
    ):
        class job_name(Person):
            def __init__(self, first_name, last_name):
                super().__init__(first_name, last_name)
                if len(inspect.getmembers(job_name)) > qualification_req:
                    del self
            pass

        self.salary = salary
        self.qualification_req = qualification_req
        self.possible_employees = possible_employees
        self.description = description
        Jobs.append(self)

DEVOPSJOB = Job("DevOps", "£5", "Jawline", 7, "Tell people how to do their jobs well")
