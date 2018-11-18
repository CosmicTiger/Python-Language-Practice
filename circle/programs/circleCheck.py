"""
 * User: lotus_zero
 * Date: 11/17/18
 * Time: 16:25 PM
 * Brief: A program to calculate Circle Area with Check
"""

PI = 3.14159

def process (radius):
    return PI * radius * radius

def main ():
    area = 0
    radius = float(input("Radius = ?\n"))

    if radius < 0:
        return area
    else:
        area = process(radius)

    return print("Area = {}".format(area))

if __name__ == ("__main__"):
    main()