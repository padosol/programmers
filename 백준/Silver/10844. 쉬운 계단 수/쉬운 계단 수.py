N = int(input())
MOD = 1_000_000_000
BIT = 1 << 10

dp = [[0] * 10 for _ in range(N + 1)]

for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, N + 1):
    for j in range(10):
        if 0 < j:
            dp[i][j] += dp[i - 1][j - 1]

        if j < 9:
            dp[i][j] += dp[i - 1][j + 1]

        dp[i][j] %= MOD

cnt = 0
for j in range(10):
    cnt += dp[N][j]
    cnt %= MOD

print(cnt)
