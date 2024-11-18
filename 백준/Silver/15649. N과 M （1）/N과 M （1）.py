N, M = map(int, input().split())


def recur(array):
    if len(array) == M:
        print(*array)
        return

    for num in range(1, N+1):
        if num not in array:
            array.append(num)
            recur(array)
            array.pop()


for i in range(1, N+1):
    recur([i])


