'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
'''
# Input the number of elements in the tuple
n = int(input())

# Initialize an empty list to hold the elements
elements = []

# Input the elements of the tuple
for _ in range(n):
    element = int(input())
    elements.append(element)

# Convert the list to a tuple
my_tuple = tuple(elements)

# Find the maximum value in the tuple
max_value = max(my_tuple)

# Output the maximum value
print(max_value)
