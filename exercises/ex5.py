# Lists 
# Implement a function that takes a list of numbers as input and returns the sum of all the even numbers in the list.

def sum_even_numbers(numbers):
    # Your code here
    result = 0
    for i in numbers:
        if i % 2 == 0:
            result = result + i
    return result
    pass


# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(numbers))  # Expected output: 30
