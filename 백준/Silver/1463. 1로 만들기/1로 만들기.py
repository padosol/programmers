n = int(input())

INF = float('inf')
dp = [INF] * (n+1)
dp[0] = 0
dp[1] = 0
for i in range(2, n+1):
    case1 = INF
    case2 = INF
    case3 = INF

    if i % 3 == 0:
        case1 = dp[i // 3] + 1

    if i % 2 == 0:
        case2 = dp[i // 2] + 1

    if i != 1:
        case3 = dp[i - 1] + 1

    dp[i] = min(case1, case2, case3)

print(dp[n])

