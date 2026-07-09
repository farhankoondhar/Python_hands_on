import math
def circle_Stats(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area,circumference
try:
    rad = float(input("Enter the radius of circle to check its area and circumference : "))
except ValueError:
    print("Invalid input")
    exit()
print("The Area and Circumference is ",circle_Stats(rad) )
