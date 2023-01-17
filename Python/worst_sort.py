import random

# Get input from user
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert input to list of integers
numbers = [int(x) for x in user_input.split()]

# Keep shuffling until the list is sorted
while numbers != sorted(numbers):
    random.shuffle(numbers)

# Print the sorted list
print(numbers)
