The goal of this code is to compute the coefficient lift of an airfoil depending
on alpha, the angle of attack. For that, various data files are given in a 
directory. My code reads the directory, finds the name of the different input 
files and computes the lift coefficient for each angle of attack. I made sure to
use key OOP concepts such as:

- Abstraction: My code is able to read any data for a specific angle of attack 
and compute the lift coefficient for it. 

- Decomposition: As well, I made sure to decompose the problem by splitting my 
code in different methods for each use case. 

- Encapsulation: Moreover, I also encapsulated several variables, which were not
accessable to the user and only accessable in the code by using the respective 
get and set methods.

Finally, I implemented several error checking and exception generation to check
that the user had provided the right path to the directory for the data files, 
that any of the required data files were found in the data directory and if an 
error was detected when reading an input file.
