def solution(food_times, k):
    foods = []
    n = len(food_times) # 음식의 갯수
    for i in range(n):
        foods.append((food_times[i], i+1))

    foods.sort()

    pretime = 0
    for i, food in enumerate(foods):
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sorted_foods = sorted(foods[i:], key=lambda x:x[1])

                return sorted_foods[k][1]
        n -= 1

    return -1