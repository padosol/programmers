N, K = map(int, input().split())

arr = []
for _ in range(N):
    name = input()
    arr.append(len(name))

len_name = [0] * 21

cnt = 0
for i in range(N):
    if K < i:
        len_name[arr[i - K - 1]] -= 1

    cnt += len_name[arr[i]]
    len_name[arr[i]] += 1

print(cnt)
