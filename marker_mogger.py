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

    def selection(self, title, options, map_dict):
        """Allows for a map to be inputted to call functions with their parameters
        Args:
            map (dict): a dict of dicts that contains a function and parameter tuple
        Returns:
            function: a function with their parameter
        """
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
        for student in self.students:
            print(f"You are now marking {student}")

program_run = Program()

mark_title = "Student Editing"
mark_options = ["Mark","Add Students from CSV","Remove students","Rearrange Students"]
mark_function_map = {

}

student_title = "Student Menu"
student_options = ["Add Students in input", "Add Students from CSV", "Remove students", "Rearrange Students"]
student_function_map = {

}

main_title = "Automated Marker"
main_options = ["Edit Students", "Begin Marking", "Edit marking scheme elements"]
main_function_map = {
    "1" : {
        program_run.selection : [student_title, student_options, student_function_map]
        },
    "2" : {
        program_run.selection : mark_function_map
    }
}

program_run.selection(main_title, main_options, main_function_map)

