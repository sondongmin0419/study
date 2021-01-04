import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(int(input()))
else:
    arr_oo = [0] * n
    arr_xo = [0] * n
    arr_ox = [0] * n
    arr_xx = [0] * n

    arr0 = int(input())
    arr1 = int(input())

    arr_oo[0] = arr0
    arr_oo[1] = arr0 + arr1

    arr_ox[0] = arr0
    arr_ox[1] = arr0

    arr_xo[0] = 0
    arr_xo[1] = arr1

    for i in range(2, n):
        arri = int(input())
        arr_ox[i] += max(arr_oo[i - 1], arr_xo[i - 1])
        arr_oo[i] += arr_xo[i - 1] + arri
        arr_xo[i] += max(arr_ox[i - 1] + arri, arr_xx[i-1] + arri)
        arr_xx[i] += max(arr_ox[i - 1], arr_xx[i - 1])
    print(max(arr_oo[n - 1], arr_xo[n - 1], arr_ox[n - 1], arr_xx[n - 1]))
