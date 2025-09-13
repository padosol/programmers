from collections import defaultdict

def solution(friends, gifts):
    gift_table = defaultdict(lambda: defaultdict(int))
    gift_index = defaultdict(int)

    answer = defaultdict(int)
    for gift in gifts:
        f, t = gift.split(" ")
        gift_table[f][t] += 1
        gift_index[f] += 1
        gift_index[t] -= 1


    size = len(friends)
    for friend_from_index in range(size):
        for friend_to_index in range(friend_from_index, size):
            friend_from = friends[friend_from_index]
            friend_to = friends[friend_to_index]
            if friend_from == friend_to:
                continue

            count_from = gift_table[friend_from][friend_to]
            count_to = gift_table[friend_to][friend_from]
            if count_from != count_to:
                # 적게 보낸 사람이 많이 보낸 사람에게 선물을 줌
                if count_from > count_to:
                    answer[friend_from] += 1
                else:
                    answer[friend_to] += 1
            else:
                index_from = gift_index[friend_from]
                index_to = gift_index[friend_to]

                if index_from != index_to:
                    if index_from < index_to:
                        answer[friend_to] += 1
                    else:
                        answer[friend_from] += 1

    
    return 0 if not answer else max(answer.values())