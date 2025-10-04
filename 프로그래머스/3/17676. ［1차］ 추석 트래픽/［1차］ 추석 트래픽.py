def str_time_to_int_time(line):
    # 환상할때는 항상 계산에 편하도록 수정해야함.
    locale_time = line[11:].split(" ")
    end_local_time = locale_time[0]
    latency = float(locale_time[1][:-1]) * 1000 - 1
    
    # 밀리세컨드 이므로 1000을 곱해줘야함
    hour_millisecond = int(end_local_time[:2]) * 60 * 60 * 1000
    minute_millisecond = int(end_local_time[3:5]) * 60 * 1000
    second_millisecond = int(end_local_time[6:8]) * 1000
    millisecond = int(end_local_time[9:])

    end_time = hour_millisecond + minute_millisecond + second_millisecond + millisecond

    return (end_time - latency, end_time)

def solution(lines):
    answer = 0

    times = []
    for line in lines:
        times.append(str_time_to_int_time(line))

    size = len(times)
    for i in range(size):
        cnt = 0
        for j in range(i, size):
            if times[i][1] + 1000 > times[j][0]:
                cnt += 1
        answer = max(answer, cnt)

    return answer