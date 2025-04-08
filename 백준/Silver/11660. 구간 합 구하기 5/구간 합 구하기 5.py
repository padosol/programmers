# 구간합 알고리즘
# 이차원 배열 구간합은 첫번째행과 열에 0을 넣어주면 계산하기 매우 편하다.
N, M = map(int, input().split())

arr = [0]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

# 이 차원 구간합 계산
prefix = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = arr[i][j]
        prefix[i][j] += prefix[i-1][j]
        prefix[i][j] += prefix[i][j-1]
        prefix[i][j] -= prefix[i-1][j-1]

# 범위 구간 합 계산
for _ in range(M):
    s1, e1, s2, e2 = map(int, input().split())

    ans = prefix[s2][e2]
    ans -= prefix[s1-1][e2]
    ans -= prefix[s2][e1-1]
    ans += prefix[s1-1][e1-1]

    print(ans)
