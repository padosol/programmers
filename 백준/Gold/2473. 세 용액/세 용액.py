N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = [1000000000, 1000000000, 1000000000]

for k in range(N):
    i = k + 1
    j = N - 1
    while i < j:
        total = arr[i] + arr[j] + arr[k]
        if abs(total) < abs(sum(answer)):
            answer = [arr[k], arr[i], arr[j]]

        if total < 0:
            i += 1
        elif total > 0:
            j -= 1
        else:
            break

print(*answer)