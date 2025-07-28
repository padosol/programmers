# 기존 RGB 에서 첫번째와 N 번째도 고려해야함

N = int(input())
rgb = []
for _ in range(N):
    rgb.append(list(map(int, input().split())))

INF = float("inf")


def solve(depth, index, start):
    if depth < 0:
        memo[depth][index] = 0
        return memo[depth][index]

    if memo[depth][index] != INF:
        return memo[depth][index]

    for i in [0, 1, 2]:
        if i != index:
            if depth == 1:
                if i != start:
                    memo[depth][index] = min(solve(depth - 1, i, start) + rgb[depth][index], memo[depth][index])
            else:
                memo[depth][index] = min(solve(depth-1, i, start) + rgb[depth][index], memo[depth][index])

    return memo[depth][index]

memo = [[INF] * 3 for _ in range(N + 1)]
red = solve(N-1, 0, 0)
memo = [[INF] * 3 for _ in range(N + 1)]
green = solve(N-1, 1, 1)
memo = [[INF] * 3 for _ in range(N + 1)]
blue = solve(N-1, 2, 2)

print(min(red, green, blue))