N = int(input())
datas = sorted(list(map(int, input().split())))

M = int(input())
cards = list(map(int, input().split()))

answers = []
for card in cards:

    s = 0
    e = N-1

    check = False
    while s <= e:
        mid = (s + e) // 2
        if datas[mid] == card:
            check = True
            break
        elif datas[mid] > card:
            e = mid - 1
        else:
            s = mid + 1

    if check:
        print(1, end=" ")
    else:
        print(0, end=" ")