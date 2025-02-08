#  ===== Assignment-19 Simple Problems on Recursion =====

# 1. Write a recursive function to calculate sum of first N natural numbers.
def sumN(n):
    if n == 1:
        return 1
    return n + sumN(n-1)
# print(sumN(5))

# 2. Write a recursive function to calculate sum of first N Odd natural numbers.
def sumOdd(n):
    if n == 1:
        return 1
    return 2*n-1 + sumOdd(n-1) 
# print(sumOdd(5))

# 3. Write a recursive function to calculate sum of first N Even natural numbers.
def sumEven(n):
    if n == 1:
        return 2
    return 2*n + sumEven(n-1)
# print(sumEven(2))

# 4. Write a recursive function to calculate factorial of a number.
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
# print(factorial(5))

# 5. Write a recursive function to calculate sum of Squares of first N natural numbers.
def sum_of_square(n):
    if n == 1:
        return 1
    return n*n + sum_of_square(n-1)
print(sum_of_square(5))