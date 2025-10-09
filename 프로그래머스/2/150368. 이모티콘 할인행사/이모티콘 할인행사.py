from itertools import product


# 가입자 늘리기
# 판매액 늘리기
def solution(users, emoticons):
    sales = [10, 20, 30, 40]
    repeat = len(emoticons)
    sales_product = list(product(sales, repeat=repeat))

    # 비율이상 모두 구매, 가격 이상 이면 구독
    result = []
    for sale in sales_product:
        # 해당 조건의 세일이 있을떄
        # 총 금액
        total_price = 0
        subscriber = 0
        for user in users:
            percent, price = user

            user_price = 0
            for i, s in enumerate(sale):
                if percent <= s:
                    user_price += emoticons[i] * (1 - (s / 100))

            if price <= user_price:
                subscriber += 1
            else:
                total_price += user_price
        result.append([subscriber, int(total_price)])
    result.sort(key=lambda x:(-x[0],-x[1]))

    return result[0]