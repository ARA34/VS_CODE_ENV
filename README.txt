This program takes a user input n and outputs an ascii block design with n blocks.
The function that does this is called blockdiag.
You can run the program by typing "python3 a0.py" in the terminal and then inputing integer n

Contact:
Alex Reyes Aranda
areyesar@uci.edu


In the refractor part of this assignment, I created a new class called Diagram.

In the Diagram class I introduce attributes iterations, and output.
The iteratrions attribute is original set to the lowest positive integer but can be changed
with the class function called "ask_input". The ask_input functions takes input from the user
converts to integer and assigns it to the iterations attribute.
This iterations attribute can then be used in the class function called blockdiag which creates
the block diagram and stores it in the class's output attribute. 
The ouput attribute is then printed out by the print_output function.