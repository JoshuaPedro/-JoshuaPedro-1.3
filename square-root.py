#square-root.py
#by Josh Pedro
#12/30/18
import math 
from math import *
def main():
    print("This program calculates the square root of a number using Newton's Method.")
    x = float(input("Enter a value to find the square root of? "))
    n = int(input("Enter the number of times to improve the guess. "))
    z = x / 2
    for i in range(n):
        z = (z+ (x / z)) / 2
    print("The final guess for the square root of ",x,"is",z)
    print("The difference from the actual square root is",math.sqrt(x)-z)
main()   