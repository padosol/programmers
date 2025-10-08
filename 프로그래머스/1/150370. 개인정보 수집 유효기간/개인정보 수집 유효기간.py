from collections import defaultdict
def to_value(today):
    year, month, day = today.split(".")
    return int(year) * 12 * 28 + int(month) * 28 + int(day)

def solution(today, terms, privacies):
    answer = []
    today = to_value(today)
    term_data = defaultdict(int)
    for term in terms:
        t, v = term.split(" ")
        term_data[t] = int(v) * 28

    for i, privacy in enumerate(privacies):
        privacy_today, privacy_type = privacy.split(" ")
        p_today_value = to_value(privacy_today)
        p_term_value = term_data[privacy_type]
        if p_today_value + p_term_value <= today:
            answer.append(i + 1)

    return answer