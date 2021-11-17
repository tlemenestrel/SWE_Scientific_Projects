import math
import re
import sys
import time

# This is an auxiliary function to sort the lines
def key_function(line):
    match = re.match('^\d+', line)
    if match:
        return int(match.group())
    else:
        return 0

# This function uses the auxiliary function key_function 
# to find the first element in each line and use it to sort the lines
def sort_file(file_name):

    with open(file_name, 'r') as file:
        lines = file.readlines()

    with open(file_name, 'w') as file:
        for line in sorted(lines, key=key_function, reverse=False):
            file.write(line)

# This function sums up the ratings of each movie and counts how many ratings 
# it has to compute the average rating of each movie
def compute_movies_average_ratings(average_movie_ratings_dict, movie_ids_list):

    for key in average_movie_ratings_dict:
        sum_movie_ratings = 0
        num_movie_ratings = 0

        for i in range(0,len(movie_ids_list)):

            if (movie_ids_list[i] == key):
                sum_movie_ratings =  sum_movie_ratings + movie_ratings[i]
                num_movie_ratings = num_movie_ratings + 1

        average_movie_ratings[key] = sum_movie_ratings / num_movie_ratings

# This function takes a dictionnary with a movie key and the associated movie
# with highest cosine similarity score and writes it as a txt file
def write_data(file_name, dictionnary):

    with open(file_name, 'w') as f: 
        for key, nested in (dictionnary.items()):
            if (len(nested) == 0):
                print('{}'.format(key), file=f)
            else:
                for subkey, value in nested.items():
                    print('{} ({},{})'.format(key, subkey, value), file=f)

if __name__ == "__main__": 
    if len(sys.argv) < 3:
        print("Usage: Please provide at least the required command line arguments, <data_file> and <output_file> ")
        print("  $ python3 echo_commands.py [arguments]")
        sys.exit(0)

start_time = time.time()

# Read the command line args, read the input file and make each column of the file into a list
input_file_name = str(sys.argv[1])
output_file_name = str(sys.argv[2])

if len(sys.argv) == 4:
    user_thresh = int(sys.argv[3])
else:
    user_thresh = 5

with open(input_file_name, "r") as input_file:
    lines = input_file.readlines()

user_ids = []
movie_ids = []
movie_ratings = []
timestamps = []

for l in lines:
         as_list = l.split('\t')
         user_ids.append(as_list[0])
         movie_ids.append(as_list[1])
         movie_ratings.append(as_list[2])
         timestamps.append(as_list[3])

number_lines = len(user_ids)
number_users = len(set(user_ids))
number_movies = len(set(movie_ids))

# Get a list of the different movie ratings and compute the average for each movie, which are stored in a dictionnary
movie_ratings = list(map(int, movie_ratings))
average_movie_ratings = {}

for i in movie_ids:
    average_movie_ratings[i] = None

compute_movies_average_ratings(average_movie_ratings, movie_ids)

# Make a dictionnary to store all the movie keys
#along with the ratings of each user for each movie (in a nested dictionnary)
movie_and_user_ratings = {}

for i in movie_ids:
    movie_and_user_ratings[i] = {}

for key in movie_and_user_ratings:

    for i in range(0,len(movie_ids)):

        if (movie_ids[i] == key):

            movie_and_user_ratings[key][user_ids[i]] = movie_ratings[i]

#Compute similarity scores
similarity_scores = {}

for i in movie_ids:
    similarity_scores[i] = {}

#Function to compute the cosine similarity scores between all the different movies. 
#Returns a dict with the match for each movie (if there is one) and the score
for keyA in movie_and_user_ratings:

    #Define an initial key and score that will be updated later every time a movie has a higher similarity score 
    best_cosine_similarity_score = -1
    best_similar_movie_key = 0

    #Separate the formula into numerator and denominator (which is itself split into the sum of the two terms squared)
    numerator_cosine_similarity_score = 0
    sum_squared_A = 0
    sum_squared_B = 0
    denominator_cosine_similarity_score = 0

    for keyB in movie_and_user_ratings:

        #If iterating over the same movie, skip the iteration
        if (keyA == keyB):
            continue

        users_in_common = list(dict(movie_and_user_ratings[keyA].items() & movie_and_user_ratings[keyB].items()).keys())

        print(users_in_common)
        
        for user in users_in_common:
            #If the number of users is less than the threshold, skip the iteration
            if (len(users_in_common) < user_thresh):
                continue
            else:
                #Update the terms of the cosine similarity formula
                sum_a = (movie_and_user_ratings[keyA][user] - average_movie_ratings[keyA])
                sum_b = (movie_and_user_ratings[keyB][user] - average_movie_ratings[keyB])
                numerator_cosine_similarity_score += sum_a * sum_b
                sum_squared_A += pow(sum_a, 2)
                sum_squared_B += pow(sum_b, 2)

        denominator_cosine_similarity_score = math.sqrt(sum_squared_A * sum_squared_B)

        #If denominator is null (to avoid dividing by 0), assign a score of -2 (that will be removed later)
        if (denominator_cosine_similarity_score == 0.0):
            cosine_similarity_score = -2
        else:    
            cosine_similarity_score = round((numerator_cosine_similarity_score / denominator_cosine_similarity_score),2)
        # If the new score is better than the previous one, update all the values
        if (cosine_similarity_score >= best_cosine_similarity_score):
            best_cosine_similarity_score = cosine_similarity_score
            largest_num_of_user_ratings = len(users_in_common)
            best_similar_movie_key = keyB
    #If the number of users is less than the threshold, append an empty dictionnary
    if (largest_num_of_user_ratings < user_thresh):
        similarity_scores[keyA] = {}
    #Stores the values (but remove the ones where score == -2, i.e. when the denominator was equal to zero)
    elif (best_cosine_similarity_score != -2):
        similarity_scores[keyA][best_similar_movie_key] = best_cosine_similarity_score

write_data(output_file_name, similarity_scores)
sort_file(output_file_name)

end_time = time.time()

elapsed_time = round((end_time - start_time), 3)
print('Input MovieLens file: ' + input_file_name)
print('Output file for similarity data: ' + output_file_name)
print('Minimum number of common users: ' + str(user_thresh))
print('Read '+ str(number_lines) + ' with total of ' + str(number_movies) + ' movies and ' + str(number_users) +  ' users')
print('Computed similarities in ' + str(elapsed_time) + ' seconds')
