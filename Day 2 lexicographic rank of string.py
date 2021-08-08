
#User function Template for python3
import math
class Solution:
    
    #Function to find lexicographic rank of a string.
    def findRank(self,S):
        s1=0
        n=len(S)
        m={}
        for i in range(n):
            if S[i] not in m:
                m[S[i]]=1
                count=0
                for j in range(i+1,n):
                    if ord(S[i])>ord(S[j]):
                        count=count+1
                s1=s1+(count*math.factorial(n-i-1))%1000003
            else:
                return 0
        return (s1+1)%1000000007
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Contributed by : Nagendra Jha
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        s=str(input())
        obj = Solution()
        print(obj.findRank(s))

# } Driver Code Ends
