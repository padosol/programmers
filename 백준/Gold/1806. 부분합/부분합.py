N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
ans = 100001
while True:
    if M <= total:
        ans = min(ans, end - start)

    if M <= total:
        total -= arr[start]
        start += 1
    else:
        if end == N:
            break

        total += arr[end]
        end += 1

print(0 if ans == 100001 else ans)

