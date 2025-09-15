def solution(numbers):
    def recur(start, end, str, answer):
        mid = (end + start) // 2


        if str[mid] == '1':
            answer[mid] = True

            if mid - 1 < start or mid + 1 > end:
                return

            recur(start, mid - 1, str, answer)
            recur(mid + 1, end, str, answer)
        else:
            # 현재 0 인데 자식노드가 있으면 False
            if mid - 1 < start or mid + 1 > end:
                answer[mid] = True
                return

            if str[(mid - 1 + start) // 2] == '1' or str[(mid + 1 + end) // 2] == '1':
                answer[mid] = False
            else:
                answer[mid] = True
                recur(start, mid - 1, str, answer)
                recur(mid + 1, end, str, answer)

    test = [2 ** i - 1 for i in range(1, 7)]
    result = []
    for n in numbers:
        num = bin(n)[2:]
        size = 0
        for t in test:
            if len(num) <= t:
                size = t
                break

        complete_str = ''.join(['0' for _ in range(size - len(num))]) + num

        answer = [False for _ in range(size)]
        start = 0
        end = size - 1
        mid = (end + start) // 2
        if complete_str[mid] == '0':
            result.append(0)
        else:
            recur(0, size-1, complete_str, answer)
            if False in answer:
                result.append(0)
            else:
                result.append(1)
    return result