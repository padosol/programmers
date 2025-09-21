def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result = arr1[i] | arr2[i]
        bin_result = str(bin(result)[2:])
        size = len(bin_result)
        rest_result = "0" * (n-size)
        bin_result = rest_result + bin_result

        data = ""
        for b in bin_result:
            if b == "1":
                data += "#"
            else:
                data += " "
        answer.append(data)
    return answer