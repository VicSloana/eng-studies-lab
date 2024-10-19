#The authors' names are Maggie, Victoria, and Anna

x = 2
if x < 3:
    print("Small")
x = 5
if x < 3:
    print("Small")
score = 8 #A score on a 10 point quiz
if score > 6:
    print("Nice work!")


for i in range(1,16):
    if i % 3 == 0:
        print(i, " is divisible by 3.")

def code():
    number = int(input("Choose a number\n"))
    if number % 2 == 0:
        print(number, "is even")
code()

x = 2
if x < 3:
    print("Small")
else:
    print("Large")
x = 5
if x < 3:
    print("Small")
else:
    print("Large")
score = 8 #A score on a 10 point quiz
if score < 6:
    print("Needs improvement")
elif score < 9:
    print("Nice work!")
else:
    print("Excellent!")

def code():
    number = int(input("Choose a number\n"))
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
code()

print(3 < 4)
print(4 > 2)
type(True)


if True:
    print("This text will always appear.")
if False:
    print("This text will not appear.")

def greater_than_10(number):
    if number > 10:
        return("True")
    else:
        return("False")
def main():
    number = int(input("Choose a number\n"))
    print(greater_than_10(number))
main()

def mood_turtle(color):
    import turtle
    riley = turtle.Turtle()
    riley.width(5)
    riley.speed(5)
    for side in range(5):
            riley.color(color)
            riley.forward(100)
            riley.right(144)
            
def main():
    mood = input("Are you feeling happy, sad, sleepy, or angry?\n")
    if mood == "happy":
        mood_turtle("pink")
    elif mood == "sad":
        mood_turtle("blue")
    elif mood == "sleepy":
        mood_turtle("green")
    else:
        mood_turtle("red")
main()


def find_divisors(n):
    total = 0
    for step in range(1, n):
        if n % step == 0:
            total = total + step
    return total

def perfect_or_not():
    n= int(input("Give me a number\n"))
    total = find_divisors(n)
    if total == n:
        return True
    else:
        return False
print(perfect_or_not())
