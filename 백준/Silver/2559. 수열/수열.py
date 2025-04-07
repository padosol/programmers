N, K = map(int, input().split())
arr = list(map(int, input().split()))

prefix = []
total = 0
for i in range(N):
    total += arr[i]
    prefix.append(total)


# 초기 값
answer = prefix[K-1]
# 2 부터 9 까지
for i in range(K, N):
    answer = max(answer, prefix[i] - prefix[i - K])

print(answer)