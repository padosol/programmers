from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []

    for c in course:
        max_cnt = 0
        result_map = defaultdict(int)
        for order in orders:
            order_list = list(order)
            response = list(combinations(order_list, c))
            for r in response:
                sorted_r = sorted(r)
                key_r = ''.join(sorted_r)
                result_map[key_r] += 1
                max_cnt = max(max_cnt, result_map[key_r])

        for key,value in result_map.items():
            if value > 1 and value == max_cnt:
                answer.append(key)

    return sorted(answer, key=lambda x: x)