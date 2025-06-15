N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

def recur(a):
    if len(a) == M:
        print(*a)
        return

    for i in range(N):
        if arr[i] not in a:
            a.append(arr[i])
            recur(a)
            a.pop()


recur([])

