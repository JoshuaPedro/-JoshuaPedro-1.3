#approximate-pi.py
#by Josh Pedro
#12/30/18
import math 
from math import *
def main():
    print("This program calculates the approximate value of pi")
    n = int(input("How many numbers would you like summed? "))
    a = 4
    x = 1
    y = float(0)
    z = float(0)
    for i in range(n):
        y = a/x
        z = z+y
        a = a*-1
        x = x+2
    print("The difference between pi and the approximate is",math.pi-z)
main()   