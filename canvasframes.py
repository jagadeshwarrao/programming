class Solution:
    def makeFrames(self, A):
        p=[]
        count=0
        s=set(A)
        if len(s)==len(A):
            return count
        else:
            for i in s:
                if A.count(i)>=4:
                    count=count+A.count(i)//4
                    if A.count(i)%4>=2:
                        p.append(i)
                elif A.count(i)>1 and A.count(i)<4:
                    p.append(i)
            count=count+len(p)//2
            return count