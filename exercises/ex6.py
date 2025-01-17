# Tuples
# Implement a function that takes a tuple of strings as input and returns a new tuple 
# containing only the strings that start with an uppercase letter.

def filter_uppercase_strings(strings):
    # Your code here
    result = []
    for element in strings:
        if element[0].isupper():
            result.append(element)
    return result
    pass


# Test the function
strings = ("Apple", "banana", "Cat", "dog", "Elephant", "Frog")
print(filter_uppercase_strings(strings))  # Expected output: ("Apple", "Cat", "Elephant")
