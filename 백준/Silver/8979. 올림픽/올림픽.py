n, k = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(n)]
medals.sort(key = lambda x: (-x[1], -x[2], -x[3]))

idx = [medals[i][0] for i in range(n)].index(k)

for i in range(n):
    if medals[idx][1:] == medals[i][1:]:
        print(i + 1)
        break