import random
import sys
import time

# Get command line arguments
if __name__ == "__main__": 

	if len(sys.argv) <= 1:

		# no arguments, print usage message
		print("Usage:")
		print("  $ python3 echo_commands.py [arguments]")
		sys.exit(0)

# Reading command line arguments
ref_file_name = sys.argv[1]
reads_file_name = sys.argv[2]
align_file_name = sys.argv[3]

# Loading and reading read and ref files
read_file = open(reads_file_name, "r")
content = read_file.read()
list_reads = content.splitlines()

ref_file = open(ref_file_name, "r")
ref = ref_file.read()

# Creating a list to store the indexes matches of the matches
matches_indexes_list = []

ref_length = len(ref)
nreads = len(list_reads)

# Defining a start value for the find function that will be updated later
start = 0

# Counting the number of occurences of each type of match
zero_match_count2 = 0
one_match_count2 = 0
two_match_count2 = 0

start_time = time.time()

for i in range (0,len(list_reads)):

	# Take a read and look for the first match with the reference
	list_of_matches = []
	read = list_reads[i]
	match = ref.find(read, 0, ref_length)

	# If no match, done with the iteration, store -1 in the list 
	if (match == -1):

			list_of_matches.append(match)
			i += 1
			zero_match_count2+=1

	else:
		# # If there is a match, store the index of the first match

		list_of_matches.append(match)

		"""
        Update the start value so the second find will not go through the full 
        reference but only after the "zone" already scanned by the first .find()
        """
		start = match

		# Look for a second match
		match = ref.find(read, start + 1, ref_length)

		# If no second match, done with the iteration
		if (match == -1):
			one_match_count2+=1

		# If there is a second match
		else:

			# Store the value and next iteration
			list_of_matches.append(match)
			two_match_count2+=1
			i += 1

	"""
    Append the indexes list for the ith read in the list that contains all the 
    indexes list in the format [[-1], [52, 68], [34], etc...]
    """
	matches_indexes_list.append(list_of_matches)

end_time = time.time()

"""
Combine the list of reads and the list of indexes. Gives a list of the format 
[[ACT, -1], [ATG, 52, 68], [ATT, 34], etc...], which is easier to write than 
having the two lists separate
"""

full_list = [[x]+y for x, y in zip(list_reads, matches_indexes_list)]

# Write the output file 
with open(align_file_name, 'w') as align_file:

    align_file.write('\n'.join(' '.join(map(str, read)) for read in full_list))

print('reference_length: ' + str(ref_length))
print('number reads: ' + str(nreads))
print('aligns 0: ' + str((zero_match_count2 / len(list_reads))))
print('aligns 1: ' + str((one_match_count2 / len(list_reads))))
print('aligns 2: ' + str((two_match_count2 / len(list_reads))))
print('elapsed time: ' + str(end_time - start_time))
