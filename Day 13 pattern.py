n=6
k=0
for i in range(n):
    number=1
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k<(((2*i)-1)//2):
            print(number,end="")
            number=number+1
        else:
            print(number,end="")
            number=number-1
    print()
        
