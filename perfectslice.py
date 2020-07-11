def solve(Andy_list):
    # write your code here
    a=len(Andy_list)
    n=int(len(Andy_list)/2)
    if(a%2==0):
        return Andy_list[0:n]
    else:
        return Andy_list[-n:]
    