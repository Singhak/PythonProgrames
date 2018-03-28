'''
pangram
a sentence containing every letter of the alphabet.
'''

def pangram(pangram_str):
	pangram_str = pangram_str.lower()
	is_pangram = True
	for alpha in "abcdefghijklmnopqrstuvwxyz":
		if alpha not in pangram_str:
			is_pangram = False
			print("\"{}\" is not a panagram".format(pangram_str))
			return
			
	print("\"{}\" is a panagram".format(pangram_str))
	
pangram("anil")
pangram("The quick brown fox jumps over the lazy dog"
