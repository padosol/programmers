A = int(input())

arr = list(map(int, input().split()))

def binary_search(arr, num):
    start = 0
    end = len(arr)

    while start < end:
        mid = (end + start) // 2

        if arr[mid] < num:
            start = mid + 1
        else:
            end = mid

    return end

def solve():

    lis = []
    for i in range(A):
        if not lis:
            lis.append(arr[i])
            continue

        if lis[-1] < arr[i]:
            lis.append(arr[i])
        else:
            mid = binary_search(lis, arr[i])
            lis[mid] = arr[i]

    return len(lis)


print(solve())


