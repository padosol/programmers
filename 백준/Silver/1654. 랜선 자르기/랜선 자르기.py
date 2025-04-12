K, N = map(int, input().split())
len_line = []
for _ in range(K):
    len_line.append(int(input()))

start = 1
end = max(len_line)
while start <= end:

    count = 0
    mid = (start + end) // 2

    for line in len_line:
        count += line // mid

    if count < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)