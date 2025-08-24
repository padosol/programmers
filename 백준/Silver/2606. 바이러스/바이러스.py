from collections import deque
computer_num = int(input())
n = int(input())

computer_network = [[] for _ in range(computer_num + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    computer_network[a].append(b)
    computer_network[b].append(a)

def bfs():
    q = deque()
    q.append(1)
    visited = [False] * (computer_num + 1)
    visited[1] = True
    count = 0

    while q:
        index = q.popleft()

        for next_index in computer_network[index]:
            if visited[next_index]:
                continue

            visited[next_index] = True
            count += 1

            q.append(next_index)



    return count

print(bfs())