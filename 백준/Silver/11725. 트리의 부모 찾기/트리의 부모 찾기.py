import sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(1, N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


root = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]


def dfs(node):
    global visited
    global root
    for n in graph[node]:
        if not visited[n]:
            visited[n] = True
            root[n] = node
            dfs(n)


dfs(1)
for i in range(2, N+1):
    print(root[i])

