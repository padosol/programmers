def solution(schedules, timelogs, startday):
    answer = 0
    
    new_schedules = []
    for schedule in schedules:
        schedule += 10
        minute = schedule % 100
        if minute >= 60:
            schedule -= minute
            schedule += 100
            minute %= 60
            schedule += minute
        
        new_schedules.append(schedule)

    for i, schedule in enumerate(new_schedules):
        flag = True
        for num, timelog in enumerate(timelogs[i]):
            day = (num + startday) % 7
            if day == 0 or day == 6:
                continue
            
            if schedule < timelog:
                flag = False
                break
        if flag:
            answer += 1
        
    return answer