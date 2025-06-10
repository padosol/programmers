N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
sum_arr = 0
ans = 0

# 투 포인터
while True:
    if sum_arr == M:
        ans += 1

    if M <= sum_arr:
        sum_arr -= arr[start]
        start += 1
    else:
        if end == N:
            break

        sum_arr += arr[end]
        end += 1

print(ans)

