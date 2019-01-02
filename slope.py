#slope.py
#By Josh Pedro
#12/13/18
def main():
    x1,y1=eval(input("Enter the first coordninate pair "))
    #asks the user to input the second y coordinate
    x2,y2=eval(input("Enter the second coordninate pair "))
    #asks the user to input th second x coordinate
    slope = ((y2-y1)/(x2-x1))
    print (slope)
main()
