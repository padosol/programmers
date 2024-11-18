N, M = map(int, input().split())


def recur(idx, array):
    if len(array) == M:
        print(*array)
        return

    for num in range(idx+1, N+1):
        array.append(num)
        recur(num, array)
        array.pop()


for i in range(1, N+1):
    recur(i, [i])


