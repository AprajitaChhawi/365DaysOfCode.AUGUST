def reverse(arr,low,high):
    while(low<high):
        arr[low],arr[high]=arr[high],arr[low]
        low=low+1
        high=high-1
def reversebyd(arr,n,d):
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
t=int(input())
while t:
    l1=list(map(int,input().split()))
    n=l1[0]
    k=l1[1]
    l=list(map(int,input().split()))
    reversebyd(l,n,k)
    print(l)
