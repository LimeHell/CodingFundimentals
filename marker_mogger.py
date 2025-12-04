""" Final Project, Generates feedback so you don't have to write as much, how wholesome!
    The goal of this project is to take some list of students, 
    allow for quick marking and then compile the markings into a zip file. 
Returns:
    A zip file with markings in
"""
#Classes
class Program:
    """Whole Program class container
    Serves for Organisation
    """
    def __init__(self):
        """Define variables to be used elsewhere
        """
        self.students = ["Jude", "Josh", "Tom"]
        self.marking_schema = ["Overall performance", "General understanding", "Contribution level", "Lab completion", "Punctuality", "Engagement", "Further study level"]

    def selection(self, title, options, map_dict):
        """Allows for a map to be inputted to call functions with their parameters
        Args:
            title (string): title of selection
            options (array): string of options
            map_dict (dict): a dict of dicts that contains a function and parameter tuple
        Returns:
            function: a function with their parameter
        """
        if title:
            print(f"--- {title}")
        for n in range(len(options)):
            print(f"-- {n+1}. {options[n]}")
        while True:
            print("-----")
            selection = input("Enter your selection: ")
            print("-----")
            try:
                function_set = []
                for function, parameter in map_dict[selection].items():
                    if parameter is None:
                        result = function()
                    else:
                        result = function(*parameter)
                    function_set.append(result)
                return function_set
            except:
                print("Invalid input! Please Try again")
                continue

    def marking(self):
        """Begins Marking Process
        """
        marking_title = False
        marking_options = self.marking_schema
        marking_function_map = {
        }
        for student in self.students:
            print(f"You are now marking {student}")
            program_run.selection(marking_title, marking_options, marking_function_map)

class Map:
    
    def __init__(self, title, options, function_map):
        self.title = title
        self.options = options
        self.function_map = function_map

class MapLibrary:
    def __init__(self):
        self.mark = Map("Student Editing", 
            ["Mark","Add Students from CSV","Remove students","Rearrange Students"], 
            {"1" : {
                program_run.marking : None,
            }})

        self.student = Map("Student Menu",
            ["Add Students in input", "Add Students from CSV", "Remove students", "Rearrange Students"],
            {})

        self.main = Map("Automated Marker",
            ["Edit Students", "Begin Marking", "Edit marking scheme elements"],
            {
                "1" : {
                program_run.selection : [self.student.title, self.student.options, self.student.function_map]
                },
                "2" : {
                program_run.selection : [self.mark.title, self.mark.options, self.mark.function_map]
                }
            }
            )

program_run = Program()
Lib = MapLibrary()
program_run.selection(Lib.main.title, Lib.main.options, Lib.main.function_map)
