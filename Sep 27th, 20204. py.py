#Sep 27th, 20204

def even_odd(x):
    if x%2==0:
        print(x, "is event.")
    else:
        print(x, "is odd.")


def countdown(n):
    if n<=0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

countdown(4)
