n=int(input())

for i in range(n):
    n1=int(input())
    ch='A'
    for  j in range(1,n1+1):
       
        for k in range(1,j+1):
            print(ch,end="")
        ch=chr(ord(ch)+1)
        print()




