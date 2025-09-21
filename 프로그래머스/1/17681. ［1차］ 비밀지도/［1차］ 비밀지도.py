def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a12 = str(bin(arr1[i] | arr2[i])[2:])
        a12 = a12.rjust(n, "0")
        a12 = a12.replace("1", "#")
        a12 = a12.replace("0", " ")
        answer.append(a12)
    return answer