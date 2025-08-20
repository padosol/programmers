from collections import deque
n, m = map(int, input().split())

singer = [[] for _ in range(n+1)]
degree = [0] * (n+1)
for _ in range(m):
    index, *arr = map(int, input().split())
    for i in range(index-1):
        a, b = arr[i], arr[i+1]
        singer[a].append(b)
        degree[b] += 1

q = deque([])
for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

answer = []
while q:
    index = q.popleft()
    answer.append(index)

    for i in singer[index]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

if len(answer) == n:
    for i in answer:
        print(i)
else:
    print(0)