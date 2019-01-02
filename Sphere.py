#Sphere.py
#JoshPedro
#12/11/18
import math
def main():
    r=eval(input("Enter the radius of the sphere. "))
    Volume=4/math.pi*r**3
    Area=4*math.pi*r**2
    print("the area of the sphere is",Area)
    print("the volume of the sphere is",Volume)
main()
