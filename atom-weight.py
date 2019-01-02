#atom-weight.py
#By JoshPedro
#12/11/18
import math
def main():
    H=eval(input("Enter the number of hydrogen atoms. "))
    C=eval(input("Enter the number of carbon atoms. "))
    O=eval(input("Enter the number of oxygen atoms. "))
    T=H*1.00794 + C*12.0107+O*15.9994 
    print("the molecular weight of the molecule is" ,T,"grams")
main()
