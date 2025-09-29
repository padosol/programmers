from itertools import permutations
def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i] + n)
    
    friends_list = list(permutations(dist, len(dist))) 
    
    for start in range(weak_len):
        for friends in friends_list:
            count = 1
            position = weak[start] + friends[count-1]
            
            for index in range(start, start + weak_len):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            
            answer = min(answer, count)
    if answer > len(dist):
        return -1

    return answer