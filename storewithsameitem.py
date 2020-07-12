class Solution:
    def countItems(self, Aname, Aprice, Bname, Bprice):
        a,b=set(Aname),set(Bname)
        c=a.intersection(b)
        d=list(c)
        count=0
        for i in range(len(d)):
            if(Aprice[Aname.index(d[i])]!=Bprice[Bname.index(d[i])]):
                count+=1
        return count