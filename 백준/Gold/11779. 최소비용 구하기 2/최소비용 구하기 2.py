import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
city = [[] for _ in range(n + 1)]
for i in range(m):
    s, e, d = map(int, input().split())
    city[s].append([d, e])

start, end = map(int, input().split())


def dijkstra(idx):
    INF = 10 ** 9

    q = [(0, idx)]
    dist = [INF] * (n + 1)
    visited = [False] * (n+1)
    
    # 초기 세팅
    dist[idx] = 0

    parent = [-1] * (n+1)
    parent[idx] = idx

    while q:
        distance, city_num = heapq.heappop(q)

        if dist[city_num] < distance:
            continue

        for next_d, num in city[city_num]:

            next_distance = distance + next_d
            if next_distance < dist[num]:
                dist[num] = next_distance
                parent[num] = city_num
                heapq.heappush(q, (next_distance, num))

    print(dist[end])
    p = end
    path = [p]
    while start != p:
        path.append(parent[p])
        p = parent[p]
    path.reverse()
    print(len(path))
    print(*path)


dijkstra(start)