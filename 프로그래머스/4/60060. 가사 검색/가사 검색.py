def solution(words, queries):
    trie = {'len': {}}
    reversed_trie = {'len': {}}

    # insert
    def insert(trie, word):
        node = trie
        for w in word:
            if w not in node:
                node[w] = {'len': {}}
            if len(word) not in node['len']:
                node['len'][len(word)] = 0
            node['len'][len(word)] += 1
            node = node[w]
        node[''] = {'len': {}}

    def select(trie, query, answer):
        cur = trie
        for i, ch in enumerate(query):
            if ch == '?':
                if len(query) in cur['len']:
                    cnt = cur['len'][len(query)]
                    answer.append(cnt)
                else:
                    answer.append(0)
                break
            elif ch not in cur:
                answer.append(0)
                break
            else:
                cur = cur[ch]

    for word in words:
        insert(trie, word)
        insert(reversed_trie, list(reversed(word)))

    # select
    answer = []
    for query in queries:
        if query[0] == '?':
            select(reversed_trie, query[::-1], answer)
        else:
            select(trie, query, answer)

    return answer