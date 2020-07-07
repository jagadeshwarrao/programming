#!/bin/python

import sys

n, q = map(int, raw_input().split())
s = [ord(k) - ord('a') for k in raw_input()]

for _ in xrange(q):
    q = map(int, raw_input().split())
    if q[0] == 1:
        for k in xrange(q[1], q[2] + 1):
            s[k] = (s[k] + q[3]) % 26
    else:
        freq = [0] * 26
        for i in xrange(q[1], q[2] + 1):
            freq[s[i]] += 1

        even = 1
        for i in xrange(26):
            if freq[i]:
                even *= 1 << (freq[i] - 1)

        ans = even - 1
        for i in xrange(26):
            if freq[i]:
                ans += (even / (1 << (freq[i] - 1))) * (1 << (freq[i] - 1)) % 1000000007

        print ans % 1000000007