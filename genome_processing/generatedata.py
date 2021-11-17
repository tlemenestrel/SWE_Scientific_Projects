import random
import sys

# Get  command line arguments
if __name__ == "__main__": 

	if len(sys.argv) <= 1:

		# no arguments, print usage message
		print("Usage:")
		print("  $ python3 echo_commands.py [arguments]")
		sys.exit(0)


# Generate the reference file
# Define the variables that we received as command line argument 

ref_length = int(sys.argv[1])
nreads = int(sys.argv[2])
read_len = int(sys.argv[3])
ref_file_name = sys.argv[4]
reads_file_name = sys.argv[5]

# For loop to generate the initial reference
ref = []
letters_list = ['A', 'C', 'G', 'T']

for i in range(0, round(0.75 * ref_length)):

	# Get a random letter from the list of letters and append it to the ref.
	# Do this as many time as the desired lenght of the reference
	random_letter = letters_list[random.randint(0,3)]
	ref.append(random_letter)

# Make the list of chars into a single string
ref = ''.join(ref)

# Copy last n characters of string to add to  ref to build last 25 %  of ref
ref_copy = ref[-round((0.25 * ref_length)):]
ref = ref + ref_copy

# Opening, writing and closing the reference file
ref_file = open(ref_file_name, "w")
ref_file.write(ref)
ref_file.close()


# Generate the reads file
# Create a list to save the reads
reads_list = []

# Create counters for the number of each type of match
zero_match_count = 0
one_match_count = 0
two_match_count = 0

for i in range(0, nreads):

	# Get a float to between 0 and 1 to do the 3 different cases in the desired percentages
	random_float = random.random()

	# Case for 1 match only (75 % of the time)
	if (0 <= random_float <= 0.75):

		# Take the first 50 % of the reference
		substring = (ref [:len(ref) // 2])

		# Define a maximum lower bound for the read
		lower_bound_max = (len(substring) - (1 + read_len))
		x = random.randint(0, lower_bound_max)

		# Extract the read from the reference
		read = substring[x:(x+read_len)]

		# Append the read to the list of reads
		reads_list.append(read)
		one_match_count +=1

	# Case for 2 matches (10 % of the time)
	elif(0.75 < random_float <= 0.85):

		# Take the last 25 % characters of the reference 
		substring = ref[-round((0.25 * ref_length)):]

		# Define a random range for the read
		idx = random.randrange(0, len(substring) - read_len + 1)

		# Get the read in the desired index from the last 25 % of the reference
		read = substring[idx : (idx+read_len)]
		reads_list.append(read)
		two_match_count +=1

	# Case for 0 match (15 % of the time)
	elif(0.85 < random_float <= 1):

		# Here, we create a while loop that will run until we find a read that 
        #does not match to the reference i.e. until .find() returns -1.
		correct_read = False

		while (correct_read == False):
			# Generate a random read using same method as for reference earlier
			random_read = []

			for i in range(0, read_len):
				random_letter = letters_list[random.randint(0,3)]
				random_read.append(random_letter)

			random_read = ''.join(random_read)

			# Check if  read matches reference, if not end of while loop, 
            # store the read and move to the next iteration
			if (ref.find(random_read) == -1):
				reads_list.append(random_read)
				zero_match_count +=1
				correct_read = True

			# Else, repeat until we get a read that does not match the reference
			else:
				pass

# Write the read file 
with open(reads_file_name, mode='w', encoding='utf-8') as read_file:

    read_file.write('\n'.join(reads_list))

print('reference_length: ' + str(ref_length))
print('number reads: ' + str(nreads))
print('read length: '+ str(read_len))

print('aligns 0: ' + str((zero_match_count / nreads)))
print('aligns 1: ' + str((one_match_count / nreads)))
print('aligns 2: ' + str((two_match_count / nreads)))
