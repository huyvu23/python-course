# write code exampale for exceptions in Python
# This code demonstrates how to handle exceptions in Python using try-except blocks.
# It includes examples of catching specific exceptions and using a finally block.
# Example 1: Basic Exception Handling
try:
    # Attempt to divide by zero
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
# Example 2: Catching Multiple Exceptions
try:
    # Attempt to convert a string to an integer
    number = int("abc")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Raise an exception: it same as throwing an exception
try:
    # Attempt to raise a custom exception
    raise ValueError("This is a custom error message.")
except ValueError as e:
    print(f"Custom Error: {e}")

try:
    # Attempt to raise a custom exception
    raise ValueError("This is a custom error message.")
except:
    print('error')


