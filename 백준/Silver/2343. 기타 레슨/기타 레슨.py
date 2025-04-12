N, M = map(int, input().split())
lecture = list(map(int, input().split()))

left, right = max(lecture), sum(lecture)

while left <= right:
    mid = (left + right) // 2
    count = 1
    total = 0
    for l in lecture:
        if total + l <= mid:
            total += l
        else:
            total = l
            count += 1

    if M < count:
        left = mid + 1
    else:
        right = mid - 1

print(left)
