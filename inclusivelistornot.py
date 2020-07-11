def solve(A):
    # write your code here
    list1=[]
    for i in range(1,len(A)-1):
        list1.append(A[i])
    if(len(A)>=6)and (A[0]+A[len(A)-1])//2 in list1:
        return True
    else:
        return False