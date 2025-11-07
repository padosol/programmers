def solution(k, score):
    answer = []
    data = []
    for c in score:
        data.append(c)
        data.sort(reverse=True)
        
        if len(data) < k:
            answer.append(data[-1])
        else:
            answer.append(data[k-1])
        
    return answer