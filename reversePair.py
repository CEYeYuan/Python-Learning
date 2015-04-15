"""
Two words are a reverse pair if each word is the reverse of
the other.
1) Write a function is_reverse_pair(s1, s2) that
returns True iff s1 and s2 are a reverse pair.
2) Write a function print_reverse_pairs(wordlist)
that accepts a list of strings and prints out all of the
reverse pairs in the given list, each pair on a line.

"""
def is_reverse_pair(s1,s2):
	"""
	string,string->bool
	"""
	if (len(s1)!=len(s2)):
		return False
	else: #do not need this 'else'
		n=len(s1)
		for i in range(n):
			if (s1[i]!=s2[n-i-1]):
				return False
		return True





def print_reverse_pairs(wordlist):
	"""
	list->None
	"""
	for word1 in wordlist:
		for word2 in wordlist:
			if (is_reverse_pair(word1,word2)):
				print (word1,word2)