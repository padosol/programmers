import heapq
INF = float("INF")
dx = (0, 0, 1, -1)
dy = (1, -1 ,0 ,0)
def dijkstra(board):
    dist = [[INF] * N for _ in range(N)]
    q = [(0,0)]
    dist[0][0] = board[0][0]

    while q:
        x, y = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                distance = dist[x][y] + board[nx][ny]
                if distance < dist[nx][ny]:
                    dist[nx][ny] = distance
                    heapq.heappush(q, (nx, ny))

    return dist[N-1][N-1]

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    ans = dijkstra(board)

    print(f'Problem {cnt}: {ans}')
    cnt += 1
