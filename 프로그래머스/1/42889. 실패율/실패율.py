def solution(N, stages):
    answer = []
    stages.sort()
    data = {i: 0 for i in range(1, N+1)}
    for stage in stages:
        if stage in data:
            data[stage] += 1
    total = len(stages)
    for i in range(1, N+1):
        result = 0 if total == 0 else data[i] / total
        answer.append((i, result))
        total -= data[i]
    answer = sorted(answer, key=lambda x: (-x[1], x))
    return [i[0] for i in answer]