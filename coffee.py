#coffee.py
#josh Pedro
#12/13/18
def main():
    pounds=eval(input("Enter the number of pounds. "))
    shipping=0.86*pounds + 1.50
    price=10.50*pounds + shipping
    price= str(price) 
    print("the price of the order is $"+price)
main()
