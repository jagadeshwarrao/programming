def largestPower(num):
    k=1
    while(k<num): # powering k with three
        k=k*3
    if(k>num):
        k=k//3
    print(k)
    
# write your code below this line #


largestPower(81)
largestPower(181)
largestPower(1881)







