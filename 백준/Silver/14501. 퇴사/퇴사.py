N = int(input())

days = [list(map(int, input().split())) for _ in range(N)]

max_money = 0

def recur(idx, money):
    global max_money

    if idx > N-1:
        if idx > N:
            return
        max_money = max(money, max_money)
        return

    # 상담을 받는 경우
    recur(idx + days[idx][0], money + days[idx][1])

    # 상담을 받지 않는 경우
    recur(idx+1, money)


recur(0, 0)
print(max_money)


