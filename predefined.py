'''
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
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

# Calculate the sum of the tuple elements
total_sum = sum(my_tuple)

# Output the sum
print(total_sum)
