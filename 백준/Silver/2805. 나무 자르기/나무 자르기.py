# 나무 수 N, 나무의 길이 M
N, M = map(int, input().split())

trees = list(map(int ,input().split()))

answer = 0

s = 0
e = max(trees)

while s <= e:
    mid = (e + s) // 2

    cut = 0
    for tree in trees:
        t = tree - mid
        if t > 0:
            cut += t

    if cut == M:
        answer = mid
        break
    elif cut > M:
        answer = max(answer, mid)
        s = mid + 1
    else:
        e = mid - 1


print(answer)







