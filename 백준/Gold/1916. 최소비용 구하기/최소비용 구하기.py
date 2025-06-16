import heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
INF = float('INF')
nodes = [INF] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])

start, end = map(int, input().split())

def dijkstra(node):
    global nodes

    visited = [False] * (N+1)

    q = [(0, node)]

    while q:
        value, node_idx = heapq.heappop(q)

        if visited[node_idx]:
            continue

        visited[node_idx] = True

        arr = graph[node_idx]
        for v, idx in arr:
            distance = value + v
            if distance < nodes[idx]:
                nodes[idx] = distance
            heapq.heappush(q, (distance, idx))


dijkstra(start)
print(nodes[end])







