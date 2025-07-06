import sys
sys.setrecursionlimit(10**6)
C, N = map(int, input().split())
city = []
for i in range(N):
    cost, customer = map(int, input().split())
    city.append([cost, customer])


INF = float('inf')
answer = INF
dp = [[0] * (C + 1) for _ in range(N + 1)]
def solve(city_num, city_customer):
    if city_num < 0:
        return INF

    if city_customer <= 0:
        return 0

    if dp[city_num][city_customer]:
        return dp[city_num][city_customer]

    case1 = solve(city_num-1, city_customer)
    case2 = solve(city_num, city_customer - city[city_num][1]) + city[city_num][0]

    dp[city_num][city_customer] = min(case1, case2)

    return dp[city_num][city_customer]

print(solve(N-1, C))