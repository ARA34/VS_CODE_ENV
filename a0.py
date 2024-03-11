"""
This module allows the user to create a digaram and interect with its functions and attributes
"""

class Diagram():
    """
    This is the class to create diagrams
    """
    def __init__(self):
        self.iterations = 1
        self.output = None

    def ask_input(self) -> None:
        """
        Asks for input from user
        """
        usr_input = int(input("Enter a positive integer: "))
        self.iterations = usr_input

    def print_output(self):
        """
        Prints the output attribute
        """
        if self.output is None:
            print("There is nothing to output")
        else:
            print(self.output)

    def blockdiag(self) -> None:
        """
        Sets the output attribute to the diagram
        """
        n = self.iterations
        # n is a positive integer
        output = ""
        top = "+-+"
        middle = "| |"
        bottom = "+-+-+"
        drop = "\n"
        tab = " "
        output += top + drop
        output += middle + drop
        for i in range(1, n):
            output += bottom + drop + (2*i) * tab
            output += middle + drop
            if i != n-1:
                output += (2*i) * tab
            else:
                output += (2*i) * tab + top
        self.output = output


c1 = Diagram()
c1.ask_input()
c1.blockdiag()
c1.print_output()
