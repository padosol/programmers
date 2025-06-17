import heapq

# N 학생, M 도로 수 , X 도착지점
N, M, X = map(int, input().split())

roads = [[] for _ in range(M + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    roads[a].append([c, b])

INF = 10 ** 9

answer = [0 for _ in range(N+1)]
def dijkstra(idx):
    global answer

    q = [(0, idx)]
    dist = [INF] * (N + 1)
    dist[idx] = 0
    visited = [False] * (N + 1)
    visited[idx] = True

    while q:
        d, n = heapq.heappop(q)
        visited[n] = True

        for rd, rn in roads[n]:
            if visited[rn]:
                continue

            nd = d + rd
            if nd < dist[rn]:
                dist[rn] = nd
                heapq.heappush(q, (nd, rn))

    answer[idx] += dist[X]
    if idx == X:
        for i in range(1, N+1):
            answer[i] += dist[i]


for i in range(1, N+1):
    dijkstra(i)

print(max(answer))