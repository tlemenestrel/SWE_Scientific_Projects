![DNA_image](https://github.com/tlemenestrel/swe_scientific_projects/blob
/master/genome_processing/dna.png)

# DNA Sequencing 

This project is a Python algorithm that is able to generate DNA references and 
compute the alignments of given DNA squences with the generated reference. This
allows to identify regions of similarity that may be a consequence of 
evolutionary relationships between the sequences. <br/>

The code generates an output file that contains the index of the matches of each 
sequence with the reference. Also, it outputs the percentage of how many matches
each sequence has (i.e. if a sequence matche once, twice or does not match the 
reference) and the computing time.

## Outputs from terminal

python3 processdata.py ref_1.txt reads_1.txt align_1.txt<br/>
reference_length: 1000<br/>
number reads: 600<br/>
aligns 0: 0.12166666666666667<br/>
aligns 1: 0.75<br/>
aligns 2: 0.12833333333333333<br/>
elapsed time: 0.003749847412109375<br/>

python3 processdata.py ref_2.txt reads_2.txt align_2.txt <br/>
reference_length: 10000<br/>
number reads: 6000<br/>
aligns 0: 0.15<br/>
aligns 1: 0.7546666666666667<br/>
aligns 2: 0.09533333333333334<br/>
elapsed time: 0.22991514205932617<br/>

$ python3 processdata.py ref_3.txt reads_3.txt align_3.txt<br/>
reference_length: 100000<br/>
number reads: 60000<br/>
aligns 0: 0.15221666666666667<br/>
aligns 1: 0.7481666666666666<br/>
aligns 2: 0.09961666666666667<br/>
elapsed time: 23.5590078830719<br/>

## Scalability

|n°| ref_l	 |  magnitude	|reads	| rlength | time   |   magnitude
|---|---|---|---|---|---|---|
|1 | 1000       |10x^3 		| 600    | 50    | 0.003 s |10x^-3
|2 | 10000      |10x^4		| 6000   | 50    | 0.1   s |10x^-1
|3 | 100000     |10x^5	    | 60000  | 50    | 23    s |10x^2
