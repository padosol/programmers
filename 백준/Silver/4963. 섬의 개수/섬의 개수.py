import sys
sys.setrecursionlimit(10**4)

dx = [0, 1, 1,  1,  0, -1,-1,-1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def bfs(y, x, yh, xw):

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < xw and 0 <= ny < yh and arr[ny][nx] == 1:
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True

            bfs(ny, nx, yh, xw)


while True:
    count = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if visited[i][j]:
                continue
            visited[i][j] = True

            num = arr[i][j]
            if num == 1:
                bfs(i, j, h, w)
                count += 1
    print(count)