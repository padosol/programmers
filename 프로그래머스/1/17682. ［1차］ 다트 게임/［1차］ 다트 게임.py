import re
def solution(dartResult):
    answer = []
    pattern = "([0-9]{1,2})([A-Z]{1})([*|#]?)"
    result = re.findall(pattern, dartResult)
    bonus_data = {
        "S": 1,
        "D": 2,
        "T": 3
    }
    for r in result:
        score, bonus, option = r

        answer.append(int(score) ** bonus_data[bonus])
        if option:
            if option == '*':
                if len(answer) == 1:
                    answer[0] *= 2
                else:
                    answer[-1] *= 2
                    answer[-2] *= 2
            else:
                answer[-1] *= -1

    return sum(answer)