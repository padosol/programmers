n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

dp = [[-1] * 3 for _ in range(n)]
def solve(num, count):
    if num < 0:
        return 0

    if count > 2:
        return 0

    if dp[num][count] != -1:
        return dp[num][count]

    # 이전에 밟음
    case1 = solve(num - 1, count + 1) + stair[num]

    # 이전안 안 밟음
    case2 = solve(num - 2, 1) + stair[num]

    dp[num][count] = max(case1, case2)

    return dp[num][count]

print(solve(n-1, 1))
