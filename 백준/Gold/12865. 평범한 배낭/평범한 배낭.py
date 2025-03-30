N, K = map(int, input().split())
w_v = [list(map(int,input().split())) for _ in range(N)]

def recur(idx, weight):
    if weight > K:
        return -9999999

    if idx == N:
        return 0

    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx][weight] = max(
        recur(idx + 1, weight + w_v[idx][0]) + w_v[idx][1],
        recur(idx + 1, weight)
    )

    return dp[idx][weight]


dp = [[-1 for _ in range(100_001)] for _ in range(N)]

print(recur(0, 0))
