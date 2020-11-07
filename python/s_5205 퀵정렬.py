def quick(arr, left, right):
    if left < right:
        p = par(arr, left, right)
        quick(arr, left, p-1)
        quick(arr, p+1, right)


def par(arr, left, right):
    i = left
    j = right
    p = arr[left]
    while i <= j:
        while arr[i] <= p and i < j:
            i += 1
        while arr[j] > p and j > i:
            j -= 1
        if i > j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


T = int(input())

for TC in range(1, T+1):

    N = int(input())

    li = list(map(int, input().split()))
    quick(li, 0, N-1)
    print(li)
