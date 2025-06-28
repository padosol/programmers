N = int(input())
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]
for i in range(N):
    data = list(map(int, input().split()))
    if i == 0:
        dp_max = [data[0], data[1], data[2]]
        dp_min = [data[0], data[1], data[2]]
        continue

    max_arr = [dp_max[0], dp_max[1], dp_max[2]]
    min_arr = [dp_min[0], dp_min[1], dp_min[2]]

    dp_max[0] = data[0] + max(max_arr[0], max_arr[1])
    dp_max[1] = data[1] + max(max_arr[0], max_arr[1], max_arr[2])
    dp_max[2] = data[2] + max(max_arr[1], max_arr[2])

    dp_min[0] = data[0] + min(min_arr[0], min_arr[1])
    dp_min[1] = data[1] + min(min_arr[0], min_arr[1], min_arr[2])
    dp_min[2] = data[2] + min(min_arr[1], min_arr[2])


print(max(dp_max), min(dp_min))


