# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1: 
        return l[0]
    return l.pop() * multiply_list(l) 

# Return the factorial of n
def factorial(n):
    if n <= 1: 
        return 1
    return n * factorial(n - 1)

# Count the number of elements in the list l
def count_list(l):
    # Define base case
    if l == []: 
        return 0
    # Recursive call + iterate
    return 1 + count_list(l[1:])

# Sum all of the elements in a list
def sum_list(l):
    # Define base case
    if l == []: 
        return 0
    # Recursive call + iterate
    return l[0] + sum_list(l[1:])

# Reverse a list without slicing or loops
def reverse(l):
    # Define base case
    if l == []: 
        return l
    # Recursive call + iterate
    return [l.pop()] + reverse(l)

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    # Define base case
    if n == 0: 
        return 0
    if n == 1: 
        return 1 
    # Recursive call + iterate
    return fibonacci(n - 1) + fibonacci(n -2)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l == []: 
        return None 
    if l[0] == i: 
        return 0
    l.pop(0)
    return 1 + find(l, i)

# Determines if a string is a palindrome
def palindrome(some_string):
    if some_string == "" or len(some_string) == 1:
        return True
    else: 
        if some_string[0] != some_string[-1]:
            return False
        return palindrome(some_string[1:-1])

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0: 
        return (width, height)
    if height > width:
        return fold_paper(width, height/2, folds - 1)
    else: 
        return fold_paper(width/2, height, folds - 1)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    print n 
    if n == target: 
        return 
    return count_up(target, n + 1)


print factorial(4)