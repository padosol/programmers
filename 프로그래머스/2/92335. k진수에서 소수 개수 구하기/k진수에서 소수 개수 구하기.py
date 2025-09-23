import math

def convert(a, b):
    convertString = '0123456789'
    sol = ''
    if a < b:
        sol = convertString[a]
    else:
        x, y = 0, 0
        while a >= b:
            x, y = divmod(a, b)
            a = x
            sol += convertString[y]
        sol += convertString[x]
    return sol[::-1]

def isPrime(a):
    a = int(a)
    if a == 0 or a == 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    result = convert(n, k)
    result = result.split("0")
    for i in result:
        if i and isPrime(i):
            answer += 1

    return answer