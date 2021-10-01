n=int(input())
for i in range(n,-1,-1):
    number=i
    for j in range(n-i):
        print(" ",end="")
    for k in range(2*i-1):
        if k<(2*i-1)//2:
            print(number,end="")
            number=number-1
        else:
            print(number,end="")
            number=number+1
    print()
