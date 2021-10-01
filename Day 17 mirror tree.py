class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def mirror(root):
    if root==None:
        return
    else:
        temp=root
        mirror(root.left)
        mirror(root.right)
        temp.left,temp.right=temp.right,temp.left
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    print("inorder of original tree")
    inorder(root)
    print()
    mirror(root)
    print("inorder of mirror tree")
    inorder(root)
