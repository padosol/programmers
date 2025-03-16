from collections import deque

# 상자 크기 m 가로, n  세로
m, n = map(int, input().split())

# 1 익은 토마토, 0 익지 않은 토마토, -1 빈 칸

box = [list(map(int, input().split())) for _ in range(n)]
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs():
    global time

    q = deque([])
    for i in range(n):
        for j in range(m):
            # 토마토가 있고 방문한 적이 없으면
            if box[i][j] == 1:
                q.append((i, j))
                visited[i][j] = True

    while True:
        if not q:
            return

        while q:
            cx, cy = q.popleft()

            for dx, dy in d:
                nx = cx + dx
                ny = cy + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and box[nx][ny] == 0:
                        box[nx][ny] = box[cx][cy] + 1
                        q.append((nx, ny))

bfs()

def check():
    time = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return 0

            time = max(box[i][j], time)
    return time

print(check() - 1)