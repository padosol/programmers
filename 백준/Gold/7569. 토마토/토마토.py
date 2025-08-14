from collections import deque
M, N, H = map(int, input().split())

box = []
for _ in range(H):

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    box.append(board)


dm = [1, -1, 0, 0, 0, 0]
dn = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

def bfs():
    q = deque()
    visited = [[[False] * M for _ in range(N)] for _ in range(H)]
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    visited[i][j][k] = True
                    q.append([i, j, k])

    while q:
        h, n, m = q.popleft()

        for i in range(6):
            nm = m + dm[i]
            nn = n + dn[i]
            nh = h + dh[i]
            if 0 <= nm < M and 0 <= nn < N and 0 <= nh < H:
                if not visited[nh][nn][nm] and box[nh][nn][nm] == 0:
                    visited[nh][nn][nm] = True
                    box[nh][nn][nm] = box[h][n][m] + 1
                    q.append([nh, nn, nm])

bfs()

success = True
answer = 0
for i in range(H):
    if not success:
        break

    for j in range(N):
        if not success:
            break

        for k in range(M):
            if box[i][j][k] == 0:
                answer = 0
                success = False
                break
            answer = max(answer, box[i][j][k])

print(answer - 1)