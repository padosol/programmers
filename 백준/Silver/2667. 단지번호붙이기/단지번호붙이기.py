N = int(input())
arr = []
for _ in range(N):
    row = list(input())
    arr.append(row)

di = (-1, 1, 0, 0)
dj = (0, 0, -1, 1)

def dfs(i, j):
    arr[i][j] = "0"
    cnt = 1

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == "1":
            cnt += dfs(ni, nj)
    return cnt

result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == "1":
            cnt = dfs(i, j)
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)
