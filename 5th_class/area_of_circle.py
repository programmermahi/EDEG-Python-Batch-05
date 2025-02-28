import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def area_of_square(side):
    return side ** 2

radius = float(input("Enter the radius of the circle: "))
side = float(input("Enter the side length of the square: "))

print("Area of the circle:", area_of_circle(radius))
print("Area of the square:", area_of_square(side))
