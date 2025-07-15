S = input()
q = int(input())
size = len(S)
for _ in range(q):
    s, l, r = input().split()
    sum_arr = [0 for _ in range(size + 1)]
    sum_arr[0] = 1 if S[0] == s else 0
    for index, value in enumerate(S):
        sum_arr[index] = sum_arr[index - 1]
        if value == s:
            sum_arr[index] += 1

    right = sum_arr[int(r)]
    left = 0 if int(l) - 1 < 0 else sum_arr[int(l) - 1]
    print(right - left)