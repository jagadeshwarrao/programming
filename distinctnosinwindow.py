class Solution:
    def dNums(self, A, B):
        res=[]
        lst=[]
        for  i in range(len(A)-B+1):
            for j in range(i,i+B):
                lst.append(A[j])
            lst=len(set(lst))
            res.append(lst)
            lst=[]
        return res