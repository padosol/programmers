N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


INF = float("inf")
color = [0, 1, 2]
memo = [[-1] * (N + 1) for _ in range(3)]
def solve(depth, index):
    if depth < 0:
        memo[index][depth] = 0
        return memo[index][depth]

    if memo[index][depth] != -1:
        return memo[index][depth]

    cost = INF
    for i in [0, 1, 2]:
        if i != index:
            cost = min(solve(depth - 1, i) + arr[depth][index], cost)

    memo[index][depth] = cost
    return memo[index][depth]

red = solve(N-1, 0)
green = solve(N-1, 1)
blue = solve(N-1, 2)
print(min(red, green, blue))