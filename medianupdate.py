from bisect import insort
from itertools import izip
from collections import Counter
import cProfile
def main():
    def find_median():
        try:
            if length%2:
                index = (length - 1)/2
                print sorted_list[index]
            else:
                index = length/2
                temp_sum = sorted_list[index]+sorted_list[index-1]
                if temp_sum % 2:
                    med = float(temp_sum)/2
                    x = round(med,1)
                else:
                    x = temp_sum // 2
                print x
        except IndexError:
            print "Wrong!"

    N = int(raw_input())

    s = []
    x = []

    for i in range(0, N):
        tmp = raw_input()
        a, b = [xx for xx in tmp.split(' ')]
        s.append(a)
        x.append(int(b))

    sorted_list = []
    unsorted_list = Counter()
    length = 0
    for cmd, param in izip(s,x):
        #print cmd, param
        #print sorted_list
        if cmd == 'a':
            length += 1
            unsorted_list[param] += 1
            insort(sorted_list,param)
        elif cmd == 'r':
            #if param in sorted_list:
            if unsorted_list[param] > 0:
                sorted_list.remove(param)
                unsorted_list[param] -= 1
                length -= 1
            else:
                print "Wrong!"
                continue
        find_median()
if __name__ == "__main__":
    main()
