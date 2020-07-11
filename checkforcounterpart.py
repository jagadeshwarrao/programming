def solve(A,k):
    # write your code here
    list1=[]
    c=k-A[0]
    for i in range(1,len(A)):
        list1.append(A[i])
    if c in list1:
        print("Exists")
    else:
        print("Doesn't Exist")