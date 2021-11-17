README.md

**Outputs from terminal:**

$ python3 similarity.py ml-100k/u.data similarities.txt
Input MovieLens file: ml-100k/u.data
Output file for similarity data: similarities.txt
Minimum number of common users: 5
Read 100000 with total of 1682 movies and 943 users
Computed similarities in 121.71 seconds

**First 10 lines of the output file:**

1 (242,0.99)
2
3
4 (435,0.88)
5 (118,0.87)
6 (242,0.95)
7 (242,0.98)
8 (242,1.0)
9 (242,1.0)
10 (242,0.98)
11 (242,0.98)

**1. What were your considerations when creating this test data?**

To create this test data, I made sure to have at least 3 movies and 10 users, saved it as test.data thus using the same format than for the real data and created a fake timestamp by using 0 for each line. I also had to be careful that each user ID was unique, while the movie IDs would repeat themselves (as one user will rate multiple movies).

**2. Were there certain characteristics of the real data and file format that you made sure to capture in your test data?**

Yes, namely saving the file as .data (like the real dataset) and using tabs to separate each values.

**3. Did you create a reference solution for your test data? If so, how?**

Yes, on my iPad, by manually computing the values for cosine similarity between each movies using the formula provided. I was then able to compare it with the output of my
code and could check that I had the same results.

**Description of the functions:**

I used 4 functions in total for this code.

The first one is key_function, an auxiliary function to sort the lines that takes a line of a file as an input. It is later used
in the 2nd function sort_file, which takes as input the name of the file to sort and sorts it according to the elements in the first
"column" of the txt file, which here is the movie id.

The 3rd function computes the average movie ratings and takes as input a dictionnary which it will use to store the values and the input
dictionnary with the movies and their ratings.

The 4th function writes the final output file and iterates over the dictionnary and its sub dictionnaries to print out the movie id, its match
(with the id) and the cosine similarity score. The file is finally according to the input filename in the .txt format.
