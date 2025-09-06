import heapq
import sys
input = sys.stdin.readline
n = int(input())

q = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            data = heapq.heappop(q)
            print(data[1])
    else:
        heapq.heappush(q, (-num, num))


