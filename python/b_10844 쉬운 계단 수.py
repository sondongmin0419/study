N = int(input())

if N == 1:
    print(9)
else:
    arr = [1] * 10
    arr[0] = 0
    for i in range(N-1):
        n_arr = [0] * 10
        n_arr[0] = arr[1]
        n_arr[9] = arr[8]
        for j in range(1,9):
            n_arr[j] = (arr[j-1] + arr[j+1]) % 1000000000
        arr = n_arr[:]
    print(sum(arr) % 1000000000)
