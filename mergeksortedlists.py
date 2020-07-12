class Solution:
    def mergeKLists(self, A):
        # write your method here
        p=[]
        for j in range(0,len(A)):  
            while(True):
                if(A[j]!=None):
                    p.append(A[j].val)
                    A[j]=A[j].next
                if(A[j]==None):
                    break
        p.sort()
        for i in p:
            print(i,end=" ")