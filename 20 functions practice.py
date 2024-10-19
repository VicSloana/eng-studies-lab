#20 Functions Practice

#PS1
def area_rectangle(w, l):
    area=w*l
    print(area)
    
area_rectangle(2, 10)

#PS2
import math
def volume(r, h):
    base = math.pi*r**2
    volume = base*h
    print(volume)

volume(10, 30)

#PS3
import math
def area_circle(r):
    area = math.pi*r**2
    return area

def area_square(s):
    area = s**2
    return area

def shadow_area(r, s):
    shadow =area_square(s) - area_circle(r)
    return shadow

print(shadow_area(1, 2))
      
#PS4
def mult_of_5(x):
    if x%5 == 0:
        print("Yes, it is")
    else:
        print("No, it is not")

mult_of_5(10)

#PS5
def maxium_of_3(x, y, z):
    result = max(x, y, z)
    print(result)

maxium_of_3(45, 23, 53)

#PS6
def minimum_of_3(x, y, z):
    result = min(x, y, z)
    print(result)

minimum_of_3(206, 405, 112)

#PS7
import math 
def maturity(time, temp, ratio):
    result = 23.7*time**3 + temp/273 + math.log(ratio)
    print(result)

maturity(10, 10, 10)

#PS8

#PS9

def BMI(lb, inch):
    result = (lb*703)/inch**2
    return result

print(BMI(120, 60))

#PS10


#PS11
def tempeture(temp):
    if temp > 78:
        print("Turn on AC")
    elif temp < 62:
        print("Turn on the heater")
    else:
        print("It's a wondeful weather")

tempeture(78)
tempeture(50)
tempeture(90)




            

      
