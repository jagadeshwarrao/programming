def solve(n):
    # write your code here
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print(' ',end='')
          
    
        for j in range(0,2*i-1):
            print('*',end='')
          
    
        for j in range(0,n-i+1):
            print(' ',end='')
        print()
        
    print((2*n+1)*'*')   
    
  