def generate_substring(sequence, length=100):
	'''Given an input string, return a random substring of length length (default 100)'''
    random_start_position = random() # from 0 to len(sequence)
	# end position needs to account for circular nature of the sequence
	#substring = sequence[random_start_position:]
	pass

def read_simulator(sequence, n, out_fasta_filename):
	# Call generate_substring() n number of times
	substring = generate_substring(sequence, 100000)
	# write substring to out_fasta_filename
	# generate fastaID for each sequence and add ">"
	pass

# call read_simulator() for each of the Mu and Wt sequences

def enumerate_kmers_in_sequence(sequence, k):
	# returns a dictionary of k-mer counts
	pass

def enumerate_kmers_in_fasta_file(k_mer_counts):
	# call enumerate_kmers_in_sequence() for each fasta sequence
	
	pass

my_wt_dict = enumerate_kmers_in_fasta_file(wt_reads)
my_mu_dict = enumerate_kmers_in_fasta_file(mu_reads)

# find differences between my_wt_dict and my_mu_dict
mu_only = set(my_mu_dict.keys()) - set(my_wt_dict.keys())
wt_only = set(my_wt_dict.keys()) - set(my_mu_dict.keys())