def solution(today, terms, privacies):
    def day_count_from_start_day(year, month, day):
        start_year = 2000
        start_month = 1
        start_day = 1
        month_day = 28
        year_day = month_day * 12

        return (year - start_year) * year_day + (month - start_month) * month_day + (day - start_day)

    privacy_map = {}
    for t in terms:
        p, d = t.split(" ")
        privacy_map[p] = int(d)

    today_split = list(map(int, today.split(".")))
    today_count = day_count_from_start_day(today_split[0], today_split[1], today_split[2])
    answer = []
    for i, p in enumerate(privacies):
        local_date, privacy = p.split(" ")
        count = privacy_map[privacy] * 28

        local_date_split = list(map(int, local_date.split(".")))
        local_count = day_count_from_start_day(local_date_split[0], local_date_split[1], local_date_split[2])
        if today_count - local_count >= count:
            answer.append(i + 1)
    return answer