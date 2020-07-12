"""
reference data types:

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""

class Solution:
    def preorderTraversal(self, A):
        if A is None:
            return
        nodeStack=[]
        nodeStack.append(A)
        while(len(nodeStack)>0):
            Treenode=nodeStack.pop()
            print(Treenode.val,end=' ')
            if(Treenode.right is not None):
                nodeStack.append(Treenode.right)
            if(Treenode.left is not None):
                nodeStack.append(Treenode.left)
        return nodeStack