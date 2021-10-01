def secondlargest(arr):
    res=-1
    largest=0
    for i in range(1,n):
        if(arr[i]>arr[largest]):
            res=largest
            largest=i
        elif(arr[i]!=arr[largest]):
            if(res==-1 or arr[i]>arr[res]):
                res=i
    return arr[res]
n=int(input())
l=list(map(int,input().split()))
print(secondlargest(l))
