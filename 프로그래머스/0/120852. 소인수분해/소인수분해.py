def solution(n):
    answer = []

    i = 1

    flag = True
    tmp = n
    while flag:
        i += 1
        if tmp % i == 0:
            if i not in answer:
                answer.append(i)
            tmp = tmp // i
            i = 1

        if i == tmp:
            flag = False
    if len(answer) == 0:
        answer.append(n)

    return answer