#User function Template for python3
class Solution:

	def immediateSmaller(self,arr,n):
	    l=[]
	    for i in range(n-1):
	        res=-1
	        if arr[i+1]<arr[i]:
	            res=arr[i+1]
	        l.append(res)
	    l.append(-1)
	    for i in range(n):
	        arr[i]=l[i]
	    return arr
		# code here

#{ 
#  Driver Code Starts

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
# } Driver Code Ends
