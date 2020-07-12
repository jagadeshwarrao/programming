m=int(input())
n=m+1
arr=[]
for i in range(m):
    s=input()
    l=list(map(int,s.split()))
    arr.append(l)

def inBound(a,b):
    if((a>=0 and a<m) and (b>=0 and b<n)):
        return True
    else:
        return False

def inRow(a,b):
    count=1
    if(inBound(a,b-1) and arr[a][b-1]==arr[a][b]):
        count+=1
    if(inBound(a,b+1) and arr[a][b+1]==arr[a][b]):
        count+=1
    if(count==3):
        return True
    else:
        return False
    
def inColumn(a,b):
    count=1
    if(inBound(a-1,b) and arr[a-1][b]==arr[a][b]):
        count+=1
    if(inBound(a+1,b) and arr[a+1][b]==arr[a][b]):
        count+=1
    if(count==3):
        return True
    else:
        return False
        

def inDiagonal(a,b):
    count=1
    if(inBound(a-1,b-1) and arr[a-1][b-1]==arr[a][b]):
        count+=1
    if(inBound(a+1,b+1) and arr[a+1][b+1]==arr[a][b]):
        count+=1
    if(count==3):
        return True
    else:
        count=1
        if(inBound(a-1,b+1) and arr[a-1][b+1]==arr[a][b]):
            count+=1
        if(inBound(a+1,b-1) and arr[a+1][b-1]==arr[a][b]):
            count+=1
        if(count==3):
            return True
        else:
            return False
        
l=[]
for i in range(m):
    for j in range(n):
        s=arr[i][j]
        if(inRow(i,j) or inColumn(i,j) or inDiagonal(i,j)):
            l.append(s)
print(min(l))









