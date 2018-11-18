"""
 * User: lotus_zero
 * Date: 11/15/18
 * Time: 23:10 PM
 * Brief: A program to calculate Circle Area
"""

PI = 3.14156

def process (radius):
    a = PI * radius * radius
    return a

def main():
    print("Radius = ?")
    radius = float(input())
    area = process(radius)
    return print("Area: {}".format(area))

if __name__ == ("__main__"):
    main()