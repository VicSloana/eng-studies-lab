#Problem 1
def print_name(name):
    print("The name is", name)

print_name("Vicky")

#Problem 2
def ninety(a, b, c):
    print((a+b+c)/3)

ninety(3, 4, 7) 

#Problem 3
def miles_per_hour(miles, hours, minutes, seconds):
    minutes = minutes/60
    seconds =seconds/3600
    result = miles/(hours+minutes+seconds)
    print("The speed is", result, "mph")

miles_per_hour(20, 2, 21, 16)

#Problem 4
def greeting(name):
    if name == "Chris":
        print("Hello", name)
    else:
        print("Goodbye", name)

greeting("Chris")
greeting("Carla")

#Problem 5
def convert_temperature(temp, units):
    if units == "Celsius":
        math = temp*(9/5)+32
        result = int(math)
        print(temp, " degrees Celsius is", result, "degrees Fahrenheit.")
    elif units == "Fahrenheit":
        math = (temp-32)*(5/9)
        result = int(math)
        print(temp, "degrees Fahrenheit is", result, "degrees Celsius.")

convert_temperature(30, "Celsius")
convert_temperature(70, "Fahrenheit")

#Problem 6
def calculate_grade(score):
    if score >= 90:
        print("A")
    if 90> score >= 80:
        print("B")
    if 80> score >= 70:
        print("C")
    if 70> score >= 60:
        print("D")
    elif score < 60:
        print("F")

calculate_grade(65)
calculate_grade(35)
calculate_grade(95)
calculate_grade(85)
calculate_grade(65)
calculate_grade(75)






