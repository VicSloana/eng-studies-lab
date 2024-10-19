
import math

def factorial(n):
    if n == 1:
        return 1
    else n > 1:
        return n*factorial(n-1)

factorial(1)
