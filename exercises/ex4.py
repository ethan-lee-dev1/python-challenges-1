# Exercise 4: Functions
# TODO: Define a function that calculates the area of a circle given its radius
import math
def main():
    # everything should be inside main()
    # create a function (calculate_area) on the next line that calculates the area of a circle. takes 1 parameter 'radius'
    def calculate_area(r):
        return math.pi * r**2

    # uncomment the following to test your code:
    radius = 5
    circle_area = calculate_area(radius)
    print("Area of the circle with radius", radius, "is:", circle_area)


main()