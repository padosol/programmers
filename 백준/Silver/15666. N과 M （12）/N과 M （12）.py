import copy
import heapq

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

answer = []
def dfs(a, idx):
    global answer
    if len(a) == M:
        b = copy.deepcopy(a)
        b.sort()
        if b not in answer:
            answer.append(b)
        return

    for i in range(idx, N):
        a.append(arr[i])
        dfs(a, i)
        a.pop()


dfs([], 0)
for ans in answer:
    print(*ans)
