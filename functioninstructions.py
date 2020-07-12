string=input()
lst=string.split(":")
s=lst[0]
rs=''
num1=int(lst[1])
num2=int(lst[2])
num3=int(lst[3])
for i in range(num1):
    s=s[-1]+s[0:len(s)-1]
for j in range(num2):
    s=s[1:]+s[0]
for i in range(len(s)):
    if(i%num3!=0):
        rs=rs+s[i]
print(rs)









