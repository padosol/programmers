def insert(word, dict):
    node = dict
    for w in word:
        if w not in node:
            node[w] = {"count": 0}
        node = node[w]
        node["count"] += 1

def search(word, dict):
    node = dict
    for index, w in enumerate(word):
        node = node[w]
        if node["count"] == 1:
            return index + 1
    return len(word)

def solution(words):
    answer = 0

    dict = {}
    for word in words:
        insert(word, dict)

    for word in words:
        answer += search(word, dict)

    return answer