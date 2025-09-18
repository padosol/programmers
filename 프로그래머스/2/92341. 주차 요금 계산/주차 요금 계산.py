import math
def solution(fees, records):
    answer = []
    data = {}
    car_order = []
    for record in records:
        time, car_num, status = record.split(" ")
        localTime = time.split(":")
        hour = int(localTime[0])
        minute = int(localTime[1])
        if car_num not in data:
            data[car_num] = {
                "total": 0,
                "start": 0,
                "isParked": False
            }
            car_order.append(car_num)
        car = data[car_num]
        if status == 'IN':
            car["start"] = hour * 60 + minute
            car["isParked"] = True
        else:
            end = hour * 60 + minute
            car["total"] += end - car["start"]
            car["isParked"] = False

    car_order.sort()
    for car_num in car_order:
        car = data[car_num]
        if car['isParked']:
            end = 23 * 60 + 59
            car["total"] += end - car["start"]
            car["isParked"] = False

        total = fees[1]
        if car["total"] - fees[0] > 0:
            total += (math.ceil((car["total"] - fees[0]) / fees[2])) * fees[3]

        answer.append(total)
    return answer