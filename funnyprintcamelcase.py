def funnyPrint(my_string):
    lis=[]
    lis=my_string.split()
    my_string2=''
    for i in range(len(lis)):
         dummy=lis[i]
         dummy=dummy.capitalize()
         my_string2=my_string2+dummy
    print(my_string2)
    
# Your code below this line #

funnyPrint("insert delete")
funnyPrint("there are two ways to LIVE")
funnyPrint("Programmer 4 lIFE")







