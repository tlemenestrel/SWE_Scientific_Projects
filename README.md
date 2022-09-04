# Software Engineering Scientific Projects

Add a list of the projects

## Genome Processing

<table>
<tr>
<td>
  
**Genome Processing** is a Python software to generate _DNA references_ and compute the alignments of given DNA sequences with the _generated reference_. 
This allows to identify **regions of similarity** that may be a consequence of _evolutionary relationships_ between the sequences. 

The code generates an **output file** that contains the index of the _matches of each sequence with the reference_ and the _percentage of how many matches
each sequence has_ (i.e. if a sequence matche once, twice or does not match the reference) and the _computing time_.

<p align="center">
<img src="https://github.com/tlemenestrel/swe_scientific_projects/blob/master/genome_processing/images/dna.jpg" width="700">
</p>

</td>
</tr>
</table>

### Alignments and references

<img src="https://github.com/tlemenestrel/swe_scientific_projects/blob/master/genome_processing/images/alignments.png" width="500">

### Terminal commands and outputs

1. First, cd into the genome_processing folder:

    ```
    $ cd genome_processing
    ```

2. Then, run the following command to process a given sequence:

    ```
    $ python processdata.py ref_3.txt reads_3.txt align_3.txt
    ```
3. You should get the following output:
    ```
    reference_length: 100000
    number reads: 60000
    aligns 0: 0.15
    aligns 1: 0.75
    aligns 2: 0.1
    elapsed time: 23.56
    ```
<details><summary><b>Show datasets and computing time</b></summary>

| Dataset | Reference length | Magnitude | Number of reads	| Reads length | Time and magnitude
|---|---|---|---|---|---|
|1 | 1000       |10<sup>3</sup>		| 600    | 50    | 0.003 s (10<sup>-3</sup>)
|2 | 10000      |10<sup>4</sup>		| 6000   | 50    | 0.1   s (10<sup>-1</sup>)
|3 | 100000     |10<sup>5</sup>	    | 60000  | 50    | 23    s (10<sup>2</sup>)

</details>

## Airfoil lift coefficient computation

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

<img src="https://github.com/tlemenestrel/swe_scientific_projects/blob/master/airfoil_computations/images/angles.png" width="500">

### Outputs

Starting from the top level directory (swe_scientific_projects), the terminal command is:

`python main.py naca0012/`<br/>
Test case: NACA 0012<br/>

|alpha  | cl      |stagnation pt|
|-----  |-------  |--------------------------|
|-3.00  |-0.3622  |( 0.0030,  0.0094)  0.9906|
| 0.00  | 0.0000  |( 0.0000,  0.0000)  0.9944|
| 3.00  | 0.3622  |( 0.0030, -0.0094)  0.9906|
| 6.00  | 0.7235  |( 0.0099, -0.0170)  0.9967|
| 9.00  | 1.0827  |( 0.0219, -0.0246)  0.9977|

<img src="https://github.com/tlemenestrel/swe_scientific_projects/blob/master/airfoil_computations/images/airfoil.png" width="500">

## Image Processing

Image processing is an important category of computations utilized in many science and engineering fields. Some important computations in image processing include focus detection and various filtering operations to smooth or sharpen an image, detect edges, etc.

The goal of this project is to developp a C++ image class that can read and write JPEG files, and has methods to compute the sharpness of the image and smooth the image using a box blur kernel of a specified size.

<img src="https://github.com/tlemenestrel/swe_scientific_projects/blob/master/image_processing/boxblur.png" width="500">

### Code description

The code first implements an image class with a constructor that accepts a string
containing the name of the JPEG file to be read. The constructor reads the file 
and stores the image data as a data attribute. It calls a function called
ReadGrayscaleJPEG(), which is pre-defined.The class also has a Save() method that writes the current version of the image 
to a JPEG file. It takes a string containing the name of the JPEG file to be 
written. However, if the string is empty the original filename is used instead.

Afterwards, the class has a Convolution() method. It has specific requirements
for both the kernel and the input and output. First, the input and output should
 be of the same size. Second, the method only supports square kernels of odd 
 sizes and at least size 3. Then, it has a BoxBlur() method that takes an argument specifying the kernel 
size and calls the Convolution() methd to smooth the image. Also, it uses a Sharpness() method that returns the sharpness of the image. 

Finally, the main file loads the image stanford.jpg and computes and outputs 
the sharpness for kernel sizes of 3, 7, . . . , 23, 27 and then compute and 
output the sharpness of the resulting images.

<img src="https://github.com/tlemenestrel/swe_scientific_projects/blob/master/image_processing/matrix.png" width="500">
