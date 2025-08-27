n = int(input())
arr = list(map(int, input().split()))

indexed_arr = list(enumerate(arr))
sorted_indexed_arr = sorted(indexed_arr, key=lambda x: x[1])

rank = 0
answer = [0] * (n)
for index, [num, value] in enumerate(sorted_indexed_arr):
    if index > 0 and sorted_indexed_arr[index-1][1] == sorted_indexed_arr[index][1]:
        answer[num] = answer[sorted_indexed_arr[index-1][0]]
    else:
        answer[num] = rank
        rank += 1

print(*answer)