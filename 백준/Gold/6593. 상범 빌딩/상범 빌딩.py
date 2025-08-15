from collections import deque
while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break


    building = []
    for l in range(L):
        field = []
        for r in range(R + 1):
            arr = list(input())
            if r != R:
                field.append(arr)
        building.append(field)

    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    q = deque()
    end = [0, 0, 0]
    for l in range(L):
        for r in range(R):
            for c in range(C):

                if building[l][r][c] == 'S':
                    q.append([l,r,c])

                if building[l][r][c] == 'E':
                    end = [l, r, c]

    dl = [0, 0, 0, 0, 1, -1]
    dr = [0, 0, 1, -1, 0, 0]
    dc = [1, -1, 0, 0, 0, 0]
    while q:
        l, r, c = q.popleft()

        for i in range(6):
            nl = l + dl[i]
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if building[nl][nr][nc] == 'E':
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                    q.clear()
                elif building[nl][nr][nc] == '.' and visited[nl][nr][nc] == 0:
                    visited[nl][nr][nc] = visited[l][r][c] + 1
                    q.append([nl, nr, nc])

    result = visited[end[0]][end[1]][end[2]]
    print('Trapped!' if result == 0 else f'Escaped in {result} minute(s).')



