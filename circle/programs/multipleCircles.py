"""
 * User: lotus_zero
 * Date: 11/17/18
 * Time: 16:25 PM
 * Brief: A program to calculate Multiple Circle Area with Check
"""

PI = 3.14159

def process (radius):
    return PI * radius * radius

def main ():
    radius = 0.0
    area = 0.0
    n = int(input("# of Circles? \n"))

    for i in range (0,n):
        radius = float(input("Circle #{}".format(i)+" Radius = ? \n"))

        if radius < 0:
            return area
        else:
            area = process(radius)

        print("Area = {}".format(area)+"\n")

    return

if __name__ == ("__main__"):
    main()