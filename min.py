'''
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
'''
# Input the number of elements
n = int(input())

# Initialize an empty list to hold the elements
elements = []

# Input the elements
for _ in range(n):
    element = int(input())
    elements.append(element)

# Convert the list to a tuple
my_tuple = tuple(elements)

# Find the minimum value in the tuple
min_value = min(my_tuple)

# Output the minimum value
print(min_value)
