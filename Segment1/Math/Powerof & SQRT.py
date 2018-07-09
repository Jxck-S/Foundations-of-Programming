# Math Module

from math import *

def main():

    num = 4.0
    exp = 2

    p = pow(num, exp)
    s = sqrt(num)

    print(str(num) + " to the power of " + str(exp) + " is " + str(p) + ".")
    print("The square root of " + str(num) + " is " + str(s) + ".")

main()