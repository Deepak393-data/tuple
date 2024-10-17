'''
Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''
# Input the tuple elements in a single line
elements = input().split()

# Convert the list of elements into a tuple
my_tuple = tuple(elements)

# Print the number of elements in the tuple
print(len(my_tuple))
