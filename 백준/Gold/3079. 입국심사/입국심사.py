# 정렬해서 max, min 구함
# 중간값
# 7 60
# 33
# 총 심사 가능 인원 구함
# 구하고자 하는 값보다 크다면 mid 를 내림
# 구하고자 하는 값보다 작다면 mid 를 올림
N, M = map(int, input().split())
task = []
for i in range(N):
    task.append(int(input()))

task.sort()

start = task[0]
end = task[N - 1] * M
min_time = end
while start <= end:
    mid = (end + start) // 2

    total = 0
    for t in task:
        total += mid // t

    if M <= total:
        end = mid - 1
        min_time = min(min_time, mid)
    else:
        start = mid + 1

print(min_time)
