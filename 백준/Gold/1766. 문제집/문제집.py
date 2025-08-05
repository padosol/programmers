import heapq

M, N = map(int, input().split())

arr = [[] for _ in range(M+1)]
degree = [0] * (M+1)
for i in range(N):
    a,b = map(int, input().split())
    arr[a].append(b)
    degree[b] += 1

q = []
for i in range(1, M+1):
    if degree[i] == 0:
        heapq.heappush(q, i)

answer = []
while q:
    index = heapq.heappop(q)

    answer.append(index)

    for num in arr[index]:
        degree[num] -= 1
        if degree[num] == 0:
            heapq.heappush(q, num)

print(*answer)
