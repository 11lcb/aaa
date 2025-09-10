import random
a=random.randint(1,100)
counts=8

while counts>0:
    A=input("give me a number between 1 to 100 \n \n")
    B=int(A)
    if B==a :
        print(" right \n ur such a genius! \n lets try a harder one")
        c=random.randint(1,2000)
        times=20
        while times>0:
            C=input("\nthe same rules,this time between 1 to 2000\n")
            D=int(C)
            if D==c:
                print("\nwhat the hell, bro!!\n goodjob! \nareu kidding me?\n")
                break
            else:
                if D<c:
                    print("\n give me a bigger one")
                if D>c:
                    print("\nok,too big\n")
                if D>2000:
                    print("\n come on bro,under 2000!:(\n")
            times=times-1                
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
while counts<=0:
    print("\ngame over:(\n seems like u should exercise more")   
    break 
print(":)\n thank u!")                

