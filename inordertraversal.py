"""
reference data types:

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""

class Solution:
    def inorderTraversal(self, A):
        # write your method here
        current=A
        ads=[]
        while(current is not None):
            
            if(current.left is None):
                #rint(current.val)
                ads.append(current.val)
                current=current.right
            else:
                pre=current.left
                while(pre.right is not None and pre.right!=current):
                    pre=pre.right
                if(pre.right is None):
                    pre.right=current
                    current=current.left
                else:
                    pre.right=None
                    #print(current.val)
                    ads.append(current.val)
                    current=current.right
        return ads