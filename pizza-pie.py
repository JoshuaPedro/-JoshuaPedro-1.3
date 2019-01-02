#pizza-pie.py
#JoshPedro
#12/11/18
import math
def main():
    d=eval(input("Enter the diameter of the pizza. "))
    p=eval(input("Enter the price of the pizza pie. "))
    Area=math.pi*(d/2)**2
    print("the area of the pizza pie is",Area)
    print("the cost per square inch is", p/Area)
main()
