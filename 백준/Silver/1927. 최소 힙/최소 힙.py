import heapq
import sys
input = sys.stdin.readline
q = []

n = int(input())
for _ in range(n):
    num = int(input())
    if num:
        heapq.heappush(q, num)
    else:
        if len(q) == 0:
            print(0)
        else:
            a = heapq.heappop(q)
            print(a)

