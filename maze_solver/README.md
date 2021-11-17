Brief statement of the problem.

The problem is the following. We need to solve a maze, given as an input txt 
file as a 2D array. For this assignment, we use the right-hand wall
following algorithm. Based on the current location and direction, the algorithm
changes direction and/or moves to a new location to find the way out.

Description of your C++ code.

The code checks if the command line arguments are provided and reads them, reads
the input file, first by reading the size of the array and then the maze. Then,
it populates the array with 0s everywhere and 1s where there is no wall. After,
it finds the entry of the maze by looking at the first row and runs a while loop
that while iterate until the exit is found. At each step, the algorithm will
attempt to go in different directions and store the positions at each step.
Finally, the positions are given in the output file and make up the solution
to the maze.

Brief summary of your code verification with ’checksoln.py‘.

The code checks if all the arguments are provided, reads the maze file and 
stores the dimensions of the maze. Then, it buils a csr matrix to store the maze 
(useful because the maze is mostly made of 0s). After, it reads the solution
file, checks that the maze was properly entered on the first row, that each 
position change is valid and that the code reaches the exit of the maze on the 
last row. Finally, it prints feedback about whether the solution is valid or 
invalid.
