from collections import deque
N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
degrees = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    degrees[b] += 1

def topological_sort():
    q = deque()
    ans = []
    for i in range(1, N+1):
        if degrees[i] == 0:
            q.append(i)

    while q:
        index = q.popleft()
        ans.append(index)

        for next_index in arr[index]:
            degrees[next_index] -= 1
            if degrees[next_index] == 0:
                q.append(next_index)

    print(*ans)

topological_sort()