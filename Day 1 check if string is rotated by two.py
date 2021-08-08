#User function Template for python3



#Function to check if a string can be obtained by rotating
#another string by exactly 2 places.
class Solution:
    def lps(self,pat,m):
        l=[]
        l.append(0)
        le=0
        i=1
        while(i<m):
            if pat[i]==pat[le]:
                l.append(le+1)
                le=le+1
                i=i+1
            else:
                if le==0:
                    l.append(0)
                    i=i+1
                else:
                    le=l[le-1]
        return l
    def isRotated(self,str1,str2):
        s=''
        s=str1+str1
        n=len(s)
        m=len(str2)
        if m==1 and str1[0]==str2[0]:
            return True
        if m==1 and str1[0]!=str2[0]:
            return False
        l=self.lps(str2,m)
        i=0
        j=0
        while(i<n):
            if s[i]==str2[j]:
                i=i+1
                j=j+1
            if j==m:
                if i-j==2 or i-j==m-2:
                    return True
                j=l[j-1]
            elif (i<n and s[i]!=str2[j]):
                if j==0:
                    i=i+1
                else:
                    j=l[j-1]
        return False
    
    #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

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
    for i in range(t):
        s=str(input())
        p=str(input())
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
