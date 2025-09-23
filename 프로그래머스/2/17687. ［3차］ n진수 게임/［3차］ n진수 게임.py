def change(a, b):
    convertString = "0123456789ABCDEF"
    sol = ''
    if a < b:
        return convertString[a]
    while a >= b:
        x, y = divmod(a, b)
        a = x
        sol += convertString[y]
    sol += convertString[x]
    return sol[::-1]

def solution(n, t, m, p):
    answer = ''
    total = t * m
    total_str = ''
    start = 0
    while len(total_str) < total:
        total_str += change(start, n)
        start += 1

    for i in range(p-1, len(total_str), m):
        answer += total_str[i]
        if len(answer) == t:
            break

    return answer