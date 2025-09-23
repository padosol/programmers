def solution(msg):
    answer = []

    index = {chr(i): i-64 for i in range(65, 91)}
    size = len(msg)

    start = 0
    end = 1
    while start < size:
        w = msg[start:end]
        if w in index:
            if end > size:
                answer.append(index[w])
                break
            end += 1
        else:
            index_num = len(index) + 1
            index[w] = index_num
            answer.append(index[w[:-1]])
            start = end - 1

    return answer