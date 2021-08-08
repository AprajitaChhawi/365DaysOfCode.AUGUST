def plusOne(A):
    num=0
    c=0
    n=len(A)
    temp=A[n-1]+1
    if temp>9:
        c=1
        A[n-1]=temp%10
        for i in range(len(A)-2,-1,-1):
            print(A[i],c)
            print(A[i]+c)
            temp=(A[i]+c)%10
            c=(A[i]+c)//10
            A[i]=temp
        if(c!=0):
            A.insert(0,c)
        print(A[0])
        while(A[0]==0):
            A.pop(0)
        return A
    else:
        A[n-1]=temp
        return A
A=[0,3,7,6,4,0,5,5,6]
print(plusOne(A))
