import sys
import bisect

for t in range(int(sys.stdin.readline().strip())):
    sys.stdin.readline()
    a_list = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    w_list = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    # minimum a for each unique w
    max_a = []
    # Map a to weights
    max_a_to_w = {}
    # Log(n) for get_total, n for add_a_w, log(n) for both is possible with balanced trees
    def get_total(a):
        if not max_a:
            return 0
        else:
            # Weight is abitrary for bisection, a is unique
            i = bisect.bisect(max_a, a)
            if i == 0 and a < max_a[i]:
                    return 0
            elif i+1 > len(max_a):
                return max_a_to_w[max_a[-1]]
            else: 
                return max_a_to_w[max_a[i-1]]
    def add_a_w(a,w):
        # Weight is abitrary for bisection, a is unique
        i = bisect.bisect_left(max_a, a)
        s = max_a[i:]
        n = 0
        for an in s:
            wn = max_a_to_w[an]
            if wn <= w:
                n += 1
            else:
                break
        del max_a[i:i+n]
        max_a.insert(i,a)
        max_a_to_w[a]=w
    for i in range(len(a_list)):
        a = a_list[i]
        w = w_list[i]
        cur_weight = get_total(a)
        prior_weight = get_total(a-1)
        take_weight = prior_weight + w
        if take_weight > cur_weight:
            add_a_w(a,take_weight)
    result = get_total(float("inf"))
    print(result)
        