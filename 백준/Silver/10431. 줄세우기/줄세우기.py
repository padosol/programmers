from collections import deque

n = int(input())
for i in range(n):
    index, *arr = list(map(int, input().split()))

    count = 0
    q = deque()
    for j in arr:
        if not q:
            q.append(j)
            continue

        next_q = deque()
        while q:
            child = q.pop()
            if j > child:
                q.append(child)
                q.append(j)
                q += next_q
                break
            else:
                count += 1
                next_q.appendleft(child)

            if not q:
                q.append(j)
                q += next_q
                break

    print(f"{index} {count}")
