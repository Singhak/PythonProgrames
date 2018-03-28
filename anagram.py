"""
anagram
a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
"""

def anagram(str1, str2):
	print("Is \"{}\" and \"{}\" is an anagram : {}".format(str1, str2, sorted(str1) == sorted(str2)))
	
anagram("anil", "nila")
