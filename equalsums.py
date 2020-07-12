def solve(A):
    # write your code here
    lst=[]
    for i in range(0,len(A)):
        s=sum(A[i])
        for j in range(i+1,len(A)):
            if(sum(A[j])==s):
                lst.append(A[i])
                lst.append(A[j])
    for i in lst:
        for j in range(0,len(i)):
            print(i[j],end=" ")
        print()