'''
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''
# Input the tuple elements in a single line
tuple_values = input().split()

# Convert the list of string values to a tuple of integers
my_tuple = tuple(map(int, tuple_values))

# Initialize a variable to hold the sum
total_sum = 0

# Calculate the sum of the elements
for value in my_tuple:
    total_sum += value

# Output the total sum
print(total_sum)
