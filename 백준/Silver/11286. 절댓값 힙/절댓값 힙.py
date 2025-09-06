import heapq
import sys
input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    num = int(input())
    if num == 0:
        print(0 if len(q) == 0 else heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(num), num))

