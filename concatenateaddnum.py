a=input()
n=[int(i) for i in a.split(',')]
m=0
k=0
s=" "
x=[ ]
num1=0
for i in range(0,len(n)):
    if(n[i]==5):
        m=i
    elif(n[i]==8):
        k=i
for i in range(0,m):
    num1=num1+n[i]
for i in range(k+1,len(n)):
    num1=num1+n[i]
for i in range(m,k+1):
    x.append(n[i])
for i in x:
    s=s+str(i)
num2=int(s)
num1=num1+num2
print(num1)




