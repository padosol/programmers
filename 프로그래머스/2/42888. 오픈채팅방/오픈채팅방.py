def solution(record):
    answer = []
    user = {}
    for re in record:
        command = re.split(" ")
        status = command[0]
        uid = command[1]
        if status == "Enter":
            user[uid] = command[2]
            answer.append((uid, 0))
        elif status == "Leave":
            answer.append((uid, 1))
        else:
            user[uid] = command[2]

    comment = ["들어왔습니다.", "나갔습니다."]
    return [user[uid] + "님이 " + comment[status] for uid, status in answer]