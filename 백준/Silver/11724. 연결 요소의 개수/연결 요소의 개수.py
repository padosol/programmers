from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)



def bfs(index):

    q = deque()
    q.append(index)

    while q:
        num = q.popleft()

        for n in arr[num]:
            if visited[n]:
                continue

            visited[n] = True
            q.append(n)


visited = [False] * (n+1)
count = 0
for i in range(1, n+1):
    if visited[i]:
        continue

    visited[i] = True
    count += 1
    bfs(i)

print(count)
