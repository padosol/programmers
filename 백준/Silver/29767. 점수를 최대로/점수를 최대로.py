# 3 -2 0 -1 3
N, K = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0 for _ in range(N)]
sum_arr[0] = arr[0]
for i in range(1, N):
    sum_arr[i] = sum_arr[i-1] + arr[i]

indexed_data = [(value, index) for (index, value) in enumerate(sum_arr)]

sorted_data = sorted(indexed_data, key=lambda x: x[0], reverse=True)

top_n_indices = [item[1] for item in sorted_data[:K]]
answer = 0
for i in top_n_indices:
    answer += sum_arr[i]

print(answer)