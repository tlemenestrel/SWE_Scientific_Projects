# Airfoil lift coefficient computation

The goal of this program is to compute the coefficient lift of an airfoil depending
on alpha, the angle of attack. For that, various data files are given in a 
directory. The code reads the directory, finds the name of the different input 
files and computes the lift coefficient for each angle of attack.  <br/>

It is able to read any data for a specific angle of attack and compute the lift coefficient for 
it. Therefore, it does not require the user to give the angles of attack as inputs,
 as the code is able to find them and output the lift coefficient for each of them.
Finally, it has several error checking and exception generation to check
that the user had provided the right path to the directory for the data files, 
that any of the required data files were found in the data directory and if an 
error was detected when reading an input file.

![Angles_image](https://github.com/tlemenestrel/swe_scientific_projects/blob/master/airfoil_computations/images/angles.png)

## Outputs

$ python main.py naca0012/<br/>
Test case: NACA 0012<br/>

|alpha  | cl      |stagnation pt|
|-----  |-------  |--------------------------|
|-3.00  |-0.3622  |( 0.0030,  0.0094)  0.9906|
| 0.00  | 0.0000  |( 0.0000,  0.0000)  0.9944|
| 3.00  | 0.3622  |( 0.0030, -0.0094)  0.9906|
| 6.00  | 0.7235  |( 0.0099, -0.0170)  0.9967|
| 9.00  | 1.0827  |( 0.0219, -0.0246)  0.9977|

![Angles_image](https://github.com/tlemenestrel/swe_scientific_projects/blob/master/airfoil_computations/images/airfoil.png)
