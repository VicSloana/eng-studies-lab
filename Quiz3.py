#The authors' names are Margaret and Victoria

#Problem 2
i = 1
sum = 0
while i < 12:
    sum += i
    i += 1
print("The sum of all numbers from 1 to 12 is", sum)
        
        
#Problem 4
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        return result

#Problem 5
def tire_pressure(pres):
    if pres < 28:
        print("Tire pressure low")
    else:
        return None

#Problem 6
def thermostat(temp):
    if temp <= 52:
        print("The heater is on")
    elif 52 < temp < 71:
        print("Heater and AC are off")
    else:
        print("AC is on")

#Problem 7
def basket(fruit):
    if fruit == "Banana":
        print("Banana it is!")
    elif fruit == "Cherry":
        print("I cherish you!")
    elif fruit == "Apple":
        print("I applesolutely like you!")
    elif fruit == "Orange":
        print("Orange you glad to see me?")
    else:
        print("You are one in a melon!")

        
