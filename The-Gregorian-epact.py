#The-Gregorian-epact.py
#By Josh Pedro
#12/13/18
import math
from math import *
def main():
    year = eval(input("Please enter a four-digit year: "))
    C = year // 100
    epact = (8 + (C // 4) - C + ((8*C + 13) // 25) + 11 * (year % 19)) % 30
    print("The value of the epact is", epact)
main()