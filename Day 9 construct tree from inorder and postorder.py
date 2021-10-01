#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    preIndex=0
    def Build(self,inorder,preorder,ini,end):
        global preIndex
        ino=0
        if ini>end:
            return None
        root=Node(preorder[self.preIndex])
        self.preIndex=self.preIndex+1
        for i in range(ini,end+1):
            if inorder[i]==root.data:
                ino=i
                break
        root.left=self.Build(inorder,preorder,ini,ino-1)
        root.right=self.Build(inorder,preorder,ino+1,end)
        return root
    def buildtree(self, inorder, preorder, n):
        ini=0
        end=n-1
        root=self.Build(inorder,preorder,ini,end)
        return root
        # code here
        # build tree and return root node


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends
