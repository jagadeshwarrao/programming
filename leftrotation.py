def read_ints():
    return list(map(int, input().strip().split()))
    
n, d = read_ints()
nums = read_ints()

nums = nums[d % n:] + nums[:d % n]
    
print(*nums)