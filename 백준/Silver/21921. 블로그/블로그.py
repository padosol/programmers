N, X = map(int, input().split())

visitor = list(map(int, input().split()))

# X-1 일수 까지 총 방문자 수 (0 일 포함)
sw = sum(visitor[:X])

max_sum = sw
# X 일 부터 N 까지
count = 1
for i in range(X, N):
    sw -= visitor[i-X]
    sw += visitor[i]

    if max_sum == sw:
        count += 1
        continue
    elif max_sum < sw:
        count = 1
        max_sum = sw


if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)

