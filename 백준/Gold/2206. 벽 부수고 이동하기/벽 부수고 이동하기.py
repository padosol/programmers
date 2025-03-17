import copy
from collections import deque

n, m = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(n)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

q = deque([(0, 0, 0)])
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1


def bfs():
    while q:
        cx, cy, block_count = q.popleft()

        if (cx, cy) == (n - 1, m - 1):
            return visited[cx][cy][block_count]

        for dx, dy in d:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < m:

                # 벽이고 벽을 부순적이 없을 경우
                if board[nx][ny] == 1 and block_count == 0:
                    visited[nx][ny][1] = visited[cx][cy][0] + 1
                    q.append((nx, ny, 1))

                # 벽이 아니고 방문한 적이 없는 경우
                elif board[nx][ny] == 0 and visited[nx][ny][block_count] == 0:
                    visited[nx][ny][block_count] = visited[cx][cy][block_count] + 1
                    q.append((nx, ny, block_count))

    return -1


print(bfs())