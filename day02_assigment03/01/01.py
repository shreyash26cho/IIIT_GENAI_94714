import math_utils as math_utils

radius = float(input("Enter the radius: "))
print("Area of Circle:", math_utils.area_circle(radius))

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
print("Area of Rectangle:", math_utils.area_rectangle(length, breadth))

base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
print("Area of Triangle:", math_utils.area_triangle(base, height))
