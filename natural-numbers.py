#natural-numbers.py
#by Josh Pedro
#12/13/18
import math 
from math import *
def main():
    print("This program calculates the sum of the first n natural numbers")
    n = int(input("enter the amount of natural numbers "))
    x = 0
    y=0
    for i in range(n):
        x=x+1
        y=y+x
    print("The sum of the first",n,"natural numbers is" ,y)
main()   
