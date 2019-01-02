#distance.py
#By Josh Pedro
#12/13/18
import math
from math import *
def main():
    x1,y1=eval(input("Enter the first coordninate pair "))
    #asks the user to input the first coordinate pair
    x2,y2= eval(input("Enter the second coordninate pair "))
    #asks the user to input th second coordinate pair
    distance = sqrt((y2-y1)**2+(x2-x1)**2)
    #takes the squared y coordinates plus the squared  x coordinates 
    print ("the distance between the two points is",distance) 
main()