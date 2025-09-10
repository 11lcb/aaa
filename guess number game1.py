import random
a=random.randint(1,100)
counts=10

while counts>0:
    A=input("give me a number between 1 to 100 \n \n")
    B=int(A)
    if B==a :
        print("right \n"*3)
        break
    else:
        if B<a :
            print("\n too small\n")
        if B>a :
            print("\n give me a smaller one\n")
        if B>100:
            print("\n between 1 to 100, remember?\n")    
        print("\n try it again!\n")    
    counts=counts-1
print(":)")                

