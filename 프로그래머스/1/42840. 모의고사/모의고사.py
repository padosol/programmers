def solution(answers):
    answer = []
    supoja = [
        {"answer": [1,2,3,4,5], "count": 0, "number": 1},
        {"answer": [2,1,2,3,2,4,2,5], "count": 0, "number": 2},
        {"answer": [3,3,1,1,2,2,4,4,5,5], "count": 0, "number": 3}
    ]

    max_count = 0
    for i in supoja:
        for j in range(len(answers)):
            a = i['answer'][j % len(i["answer"])]
            b = answers[j % len(answers)]
            if a == b:
                i['count'] += 1
        max_count = max(max_count, i['count'])

    for i in supoja:
        if max_count == i['count']:
            answer.append(i['number'])
    answer.sort()

    return answer