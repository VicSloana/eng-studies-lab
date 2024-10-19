# A code that asks the user for a number and prints out "Even" if the number is even, and
prints out "Odd" otherwise.
def even(n):
    if n%2 == 0:
        return "is even"
    else:
        return "is not even"

def ask_number():
    n = int(input("Type a number: "))
    print(n, even(n))

ask_number()


#A function that takes a number as an input and returns True if it is greater than 10 and False otherwise

def greater_10(n):
    if n > 10:
        return True
    else:
        return False

def main():
    n = int(input("Type a number: "))
    print(greater_10(n))

main()
    
#
