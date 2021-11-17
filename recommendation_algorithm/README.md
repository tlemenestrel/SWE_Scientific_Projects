# Recommendation algorithm

![Recc_image](https://github.com/tlemenestrel/swe_scientific_projects/blob/master/recommendation_algorithm/images/cosine.png)

**Outputs from terminal:**

$ python3 similarity.py ml-100k/u.data similarities.txt<br/>
Input MovieLens file: ml-100k/u.data<br/>
Output file for similarity data: similarities.txt<br/>
Minimum number of common users: 5<br/>
Read 100000 with total of 1682 movies and 943 users<br/>
Computed similarities in 121.71 seconds<br/>

## First 10 lines of the output file:

1 (242,0.99)<br/>
2<br/>
3<br/>
4 (435,0.88)<br/>
5 (118,0.87)<br/>
6 (242,0.95)<br/>
7 (242,0.98)<br/>
8 (242,1.0)<br/>
9 (242,1.0)<br/>
10 (242,0.98)<br/>
11 (242,0.98)<br/>

## Functions 

I used 4 functions in total for this code.

The first one is key_function, an auxiliary function to sort the lines that takes a line of a file as an input. It is later used<br/>
in the 2nd function sort_file, which takes as input the name of the file to sort and sorts it according to the elements in the first<br/>
"column" of the txt file, which here is the movie id.<br/>

The 3rd function computes the average movie ratings and takes as input a dictionnary which it will use to store the values and the input<br/>
dictionnary with the movies and their ratings.<br/>

The 4th function writes the final output file and iterates over the dictionnary and its sub dictionnaries to print out the movie id, its match<br/>
(with the id) and the cosine similarity score. The file is finally according to the input filename in the .txt format.<br/>
