def recur(idx, weight):
    if weight > K :
        return -99999
    if idx == N :
        return 0 
    if dp[idx][weight] != -1:
        return dp[idx][weight]
    
    dp[idx][weight] = max(recur(idx + 1, weight + items[idx][0]) + items[idx][1], recur(idx + 1, weight))
    return dp[idx][weight]

N,K = map(int,input().split())
items = [list(map(int,input().split())) for _ in range(N)]
#무게를 고려해서 가치를 담는 dp테이블, 무게는 얼마든지 커질 수 있으므로 10만, 그리고 물건개수만큼 N 작성
dp = [[-1 for _ in range(100_001)] for _ in range(N)]

print(recur(0,0))