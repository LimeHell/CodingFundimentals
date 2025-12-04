""" Final Project, Generates feedback so you don't have to write as much, how wholesome!
    The goal of this project is to take some list of students, allow for quick marking and then compile the markings into a zip file. 
Returns:
    A zip file with markings in
"""
#Classes
class Program:
    
    def __init__(self):
        """Define variables to be used elsewhere
        """
        self.students = ["Jude", "Josh", "Tom"]
    
    def selection(self, map):
        """Allows for a map to be inputed to call functions with their parameters

        Args:
            map (dict): a dict of dicts that contains a function and parameter tuple

        Returns:
            function: a function with their parameter
        """
        while True:
            print("-----")
            selection = input("Enter your selection: ")
            print("-----")
            try:
                function_set = []
                for function, parameter in map[selection].items():
                    if parameter is None:
                        result = function()
                    else:
                        result = function(parameter)
                    function_set.append(result)
                return function_set
            except:
                print("Invalid input! Please Try again")
                continue

    def main_menu(self):
        """Presents a main menu to the user showing all the functions of the script
        This ensures the user has access to the functionality of the script and gives the ability to ignore unwanted functions
        """
        print("--- Automated Marker")
        print("-- 1. Edit Students")
        print("-- 2. Begin Marking")
        print("-- 3. Edit marking scheme elements")

    def edit_students_menu(self):
        """Presents options to edit student details
        This allows for comprehensive changes to student list
        """
        print("--- Student Editing")
        print("-- 1. Add Students in input")
        print("-- 2. Add Students from CSV")
        print("-- 3. Remove students")
        print("-- 4. Rearrange Students")

    def marking_menu(self):
        """Menu for marking functions
        Allows for interacting with marking functionalities
        """
        for student in self.students:
            print(f"You are now marking {student}")
            print("--- Student Editing")
            print("-- 1. Mark")
            print("-- 2. Add Students from CSV")
            print("-- 3. Remove students")
            print("-- 4. Rearrange Students")

program_run = Program()

program_run.main_menu()
mark_function_map = {
    
}
esm_function_map = {
    
}
mm_function_map = {
    "1" : {
        program_run.edit_students_menu : None, 
        program_run.selection : esm_function_map
        },
    "2" : {
        program_run.marking_menu : None,
        program_run.selection : mark_function_map
    }
}

program_run.selection(mm_function_map)