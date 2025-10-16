def solution(n, w, num):
    answer = 0
    
    num -= 1
    
    line_num = num // w
    index = 0
    if line_num % 2 == 0:
        index = num % w
    else:
        index = w - (num % w) - 1
    
    while True:
        line_num += 1

        # 홀수 층
        if line_num % 2 == 0:
            if line_num * w + index + 1 > n:
                break
        # 짝수 층
        else:
            if line_num * w + (w - index) > n:
                break
                
        answer += 1
    
    return answer + 1