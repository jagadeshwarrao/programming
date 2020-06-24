#InfyTQ - Colorful Number
#A number is a COLORFUL number, if the product of every digit of a contiguous subsequence is different.

#A number can be broken into different contiguous sub-subsequence parts.

#Suppose, a number = 3245, it can be broken into parts like 3 2 4 5 32 24 45 324 245 and since the product of every digit of a contiguous subsequence is different therefore 3245 is COLORFUL number.

#Given a number A, return 1 if A is COLORFUL else return 0.

#Input :3245

#Output :1








class Solution:
    def colorful(self, A):
        # write your method here
        l1=list(str(A))
        #return s
        l=[]
        s=""
        for i in range(len(l1)+1):
            for j in range(i+1,len(l1)+1):
                s1=[]
                s1.extend(l1[i:j])
                #print(s1)
                a=1
                for k in s1:
                    a*=int(k)
                l.append(a)
        for i in l:
            s=s+str(i)
        for i in l:
            if s.count(str(i))==1:
                return 1
            else:
                return 0