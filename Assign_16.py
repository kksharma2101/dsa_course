#  ===== Assignment-18 Simple Problem of Recursion =====

# 1. Write a recursive function to print first N natural numbers.
def printN(n):
    if n > 0:
        printN(n-1)
        print(n, end=' ')
# printN(10)

# 2. Write a recursive function to print first N natural numbers in reverse order.
def printReverse(n):
    if n > 0:
        print(n, end=' ')
        printReverse(n-1)
# printReverse(11)

# 3. Write a recursive function to print first N Odd natural numbers.
def printOdd(n):
    if n > 0:
        printOdd(n-1)
        print(n*2-1, end=' ')
# printOdd(10)

# 4. Write a recursive function to print first N Even natural numbers.
def printEven(n):
    if n > 0:
        printEven(n-1)
        print(n*2, end=' ')
# printEven(5)

# 5. Write a recursive function to print first N Odd natural numbers in reverse oreder.
def printOddReverse(n):
    if n > 0:
        print(n * 2 - 1, end=' ')
        printOddReverse(n-1)
# printOddReverse(8)

# 6. Write a recursive function to print first N Even natural numbers in reverse oreder.
def printEvenReverse(n):
    if n > 0:
        print(n*2, end=' ')
        printEvenReverse(n-1)
printEvenReverse(9)