class Solution:
    def isBalanced(self, s):
        # write your method here
        l=[]
        self.s=s
        for i in range(0,len(self.s)):
            if(self.s[i]=='{' or self.s[i]=='[' or self.s[i]=='('):
                l.append(self.s[i])
            elif(self.s[i]=='}' or self.s[i]==']' or self.s[i]==')'):
                if(len(l)>0):
                    p=l.pop()
                    if(p=='{' and self.s[i]!='}'):
                        return 0
                    elif(p=='['and self.s[i]!=']'):
                        return 0
                    elif(p=='('and self.s[i]!=')'):
                        return 0
                   
                else:
                    return 0
        if(len(l)!=0):
            return 0
        else:
            return 1