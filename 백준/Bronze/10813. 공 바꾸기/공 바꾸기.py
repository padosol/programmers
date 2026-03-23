N, M = map(int, input().split())

bag = list(range(N+1))
for _ in range(M):
    i, j = map(int, input().split())
    bag[i], bag[j] = bag[j], bag[i]

print(*bag[1:])


