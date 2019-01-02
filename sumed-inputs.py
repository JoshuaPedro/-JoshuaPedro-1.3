#sumed-inputs.py
#by Josh Pedro
#12/30/18
import math 
from math import *
def main():
    print("This program will find the average of a series of numbers entered.")
    n = int(input("How many numbers would you to enter? "))
    x = 0
    y = 0
    for i in range(n):
        x = int(input("Enter number. "))
        y = y+x
    print("The average of the ",n," numbers entered is ",y)
main()   