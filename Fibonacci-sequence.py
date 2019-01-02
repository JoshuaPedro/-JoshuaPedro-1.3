#Fibonacci-sequence.py
#by Josh Pedro
#12/30/18
import math 
from math import *
def main():
    print("This program calculates the Fibonacci sequence")
    n = int(input("How many Fibonacci numbers would you like? "))
    x = 1
    y = 0
    z = 0
    for i in range(n):
        z = x+y
        x = y
        y = z
    print("The fibonacci number",n,"is",z)
main()   