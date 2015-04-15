"""
Write a function print_record that takes a dictionary as input.
Keys are student numbers ( int ), values are names ( str ). The
function should print out all records, nicely formatted.
>>> record = {1234: 'Tony Stark', 1138: 'Steve Rogers'}
>>> print_record(record)
Tony Stark (#1234)
Steve Rogers (#1138)
Write a function count_occurrences that takes an open file as
input, and returns a dictionary with key/value pairs of each word
and the number of occurrences of that word. (a word is a white-
space delimited token, and can have punctuation)
>>> open_file = io.StringIO('a b a a c c a.')
>>> count_occurences(open_file)
{'a': 3, 'b': 1, 'a.': 1, 'c': 2}
"""

def print_record(record):
	"""
	dict->None
	"""
	for key in record:
		print("{} (#{})".format(record[key],key))


def count_occurrences(file):
	"""
	open_file->dict
	"""
	dic={}
	for line in file:
		for word in (line.split()):
			if word in dic:
				dic[word]+=1
			else:
				dic[word]=1
	return dic