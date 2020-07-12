"""
reference data types:

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
def peek(stack): 
        if len(stack) > 0: 
            return stack[-1] 
        return None
class Solution:
    def postorderTraversal(self, A):
        # write your method here
        ans=[]
        if A is None:
            return
        stack=[]
        while(True):
            while(A):
                if(A.right is not None):
                    stack.append(A.right)
                stack.append(A)
                A=A.left
            A=stack.pop()
            if (A.right is not None and peek(stack) == A.right):
                stack.pop()
                stack.append(A)
                A=A.right
            else:
                ans.append(A.val)
                A=None
            if(len(stack)<=0):
                break
        return ans