def switcher(c):
        v={'}':'{',']':'[',')':'('}
        return v[c]

#program starts
s=input()
n=len(s)%2
l=[]            #list for pushing opening braces
x=1
m=0              #to know unbalnced brace position
if(len(s)==0):
    x=0
    
elif(n!=0):          #length odd
    if(s[0]=='}' or s[0]==')' or s[0]==']'):                  #starting char is opening brace
        m=1
    else:
        for i in s:
            m+=1
            if(i=='{' or i=='[' or i=='('):
                l.append(i)
            elif(i=='}' or i==')' or i==']'):
                if(switcher(i)==l.pop()):
                    x=0
                else:
                    break
        if(m==len(s)):
            m=len(s)+1
            
else:            #length even
    if(s[0]=='}' or s[0]==')' or s[0]==']'):                  #starting char is opening brace
        m=1
    else:
        for i in s:
            m+=1
            if(i=='{' or i=='[' or i=='('):
                l.append(i)
            elif(i=='}' or i==')' or i==']'):
                if(switcher(i)==l.pop()):
                    x=0
                else:
                    break
if(x==0 and len(l)==0):
    print(0)
else:
    print(m)









