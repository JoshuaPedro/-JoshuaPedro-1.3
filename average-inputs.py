#average-inputs.py
#by Josh Pedro
#12/30/18
import math 
from math import *
def main():
    print("This program will find the average of a series of numbers entered.")
    n = int(input("How many numbers would you like to enter? "))
    x = 0
    y = 0
    z = 0
    for i in range(n):
        x = float(input("Enter number => "))
        y = y+x
    z = float(y // n)
    print("The avarage of the numbers entered is",z)
main()   