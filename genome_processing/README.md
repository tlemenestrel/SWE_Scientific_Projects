README.md

**Outputs from terminal:**

$ python3 generatedata.py 1000 600 50 "ref_1.txt" "reads_1.txt"
reference_length: 1000
number reads: 600
read length: 50
aligns 0: 0.12166666666666667
aligns 1: 0.75
aligns 2: 0.12833333333333333

$ python3 generatedata.py 10000 6000 50 "ref_2.txt" "reads_2.txt"
reference_length: 10000
number reads: 6000
read length: 50
aligns 0: 0.15
aligns 1: 0.7546666666666667
aligns 2: 0.09533333333333334

$ python3 generatedata.py 100000 60000 50 "ref_3.txt" "reads_3.txt"
reference_length: 100000
number reads: 60000
read length: 50
aligns 0: 0.15221666666666667
aligns 1: 0.7481666666666666
aligns 2: 0.09961666666666667

**• Describe in a paragraph or so the considerations you used in designing your handwritten test data. If
your code works properly for your handwritten data, will it always work correctly for other datasets?**

For the handwritten test data, I made sure to only use the letters A, C, T and G. I also used the correct dimensions specified
i.e. length of reference 10 and 5 reads of length 3. In this case, the coode should work for other datasets, as they are all in the 
same format, the only difference is in the size.

**• Should you expect an exact 15% / 75% / 10% distribution for the reads that align zero, one, and two times? 
What other factors will affect the exact distribution of the reads?**

The distribution will always be close to those numbers but might vary slighty. It will vary more if the dataset is smaller. That
is because of the law of large numbers. The larger the sample size, the closer we get to the distribution.

**• How much time did you spend writing the code for this part?**

Overall, I spent 1h30 on this part, spent between prototyping a solution on my iPad, writing pseudocode,
building the soolution and adding the comments.

**Outputs from terminal:**

python3 processdata.py ref_1.txt reads_1.txt align_1.txt
reference_length: 1000
number reads: 600
aligns 0: 0.12166666666666667
aligns 1: 0.75
aligns 2: 0.12833333333333333
elapsed time: 0.003749847412109375

python3 processdata.py ref_2.txt reads_2.txt align_2.txt
reference_length: 10000
number reads: 6000
aligns 0: 0.15
aligns 1: 0.7546666666666667
aligns 2: 0.09533333333333334
elapsed time: 0.22991514205932617

$ python3 processdata.py ref_3.txt reads_3.txt align_3.txt
reference_length: 100000
number reads: 60000
aligns 0: 0.15221666666666667
aligns 1: 0.7481666666666666
aligns 2: 0.09961666666666667
elapsed time: 23.5590078830719

**• Does the distribution of reads that align zero, one, and two or more times exactly match the distributions you computed as you were creating the datasets? Why or why not?**

The distribution of reads matches the one computed when creating the datasets, which is because they were not modified between each steps of the process.

**• Using your timing results what can you say about the scalability of your implementation as the size of the reference and read length varies? Estimate the time to align the data for a human at 30x coverage and a read length of 50. Put differently, we’d like you estimate the growth rate of the time it takes your program to process inputs as a function of input size, where the input size is determined by the reference length and the number of reads (notice that in table 1, the number of reads increases proportional to the increase in the reference length: we ask that you carry this over to the writeup problem, i.e. what is the expected increase in runtime when the reference length increases (with a corresponding increase in the number of reads). Ultimately, we want you to answer the following question: is it feasible to actually analyze all the data for a human using your program?**

I ran additional tests with the code and got the following results:

|n°| ref_l	 |  magnitude	|reads	| rlength | time   |   magnitude
|---|---|---|---|---|---|---|
|1 | 1000       |10x^3 		| 600    | 50    | 0.003 s |10x^-3
|2 | 10000      |10x^4		| 6000   | 50    | 0.1   s |10x^-1
|3 | 100000     |10x^5	    | 60000  | 50    | 23    s |10x^2
|4 | 3x10^9     |10x^9		| 18x10^8| 50    | ?     s |10x^17

3x10^9 is the size of the human genome i.e. what we want to estimate. We see that for an increase by 1 in the order of magnitude of the length of the reference and a corresponding increase in the number of reads, we have an increase by 2 in the order of magnitude of the time to process the data. Therefore, the time to parse the human genome
would approximately be of magnitude 10x^17, which is equal to 3x10^9 days. Therefore, it is not feasible to analyze all the data of a human using this program.

**• How much time did you spend writing the code for this part?**

Overall, I spent 2 hours on this part, spent similarly than for the first part, i.e.
prototyping a solution on my iPad, writing pseudocode, building the soolution and 
adding the comments. I also spent additional time on the writeup to find an estimate
for the second question of the writeup.
