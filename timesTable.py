"""
Compute (and store in a variable) a times table
for the numbers 0 through 9 as a list of lists.
For example, if it were just from 0 through 2,
you should create:
[[0, 0, 0],
[0, 1, 2],
[0, 2, 4]]

"""
#Approach 1
table1 = []
n = 10 # from 0 to (n - 1)
for i in range(n):
# Compute the n'th row
	row = []
	for j in range(n):
		row.append(i * j)
# Add row to full table
	table1.append(row)

#Approach 2 Both works!
table2 = []
n = 10 # from 0 to (n - 1)
for i in range(n):
# Compute the n'th row
	row = []
# Add row to full table
	table2.append(row)
	for j in range(n):
		row.append(i * j)