"""
 * User: lotus_zero
 * Date: 11/17/18
 * Time: 18:33 PM
 * Brief: A program to calculate Multiple Indeterminated # of Circle Area with Check
"""

PI = 3.14159

def process(radius):
    return PI * radius * radius

def main():
    area = 0
    print("TO STOP THE PROGRAM. ENTER 0 AS VALUE OF RADIUS")
    radius = float(input("Radius = ?\n"))

    #@code generator expressions is used to generate a minimum code to facilitate conditions or process
    #@code that are a bit more complex or that python doesn't allow normally
    gen = ("if radius != 0:  return in range(0, 1) else: return in range(0, 0)")

    for i in gen:
        if radius < 0:
            return area
            n = 0
        else:
            area = process(radius)

        print("Area = {}".format(area)+"\n")

        radius = float(input("Radius = ?\n"))

    return

if __name__ == ("__main__"):
    main()