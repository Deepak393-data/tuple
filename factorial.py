'''
Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
# Input the tuple elements in a single line
tuple_values = input().split()

# Convert the list of string values to a tuple of integers
my_tuple = tuple(map(int, tuple_values))

# Input the number to count
x = int(input())

# Count the occurrences of x in the tuple
count = my_tuple.count(x)

# Function to calculate factorial without using factorial() method
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Output the count and its factorial
print(count)
print(factorial(count))
