li = list(map(int, list(input())))

while li:
    sum = 0
    for i in range(7):
        a = li.pop(0)
        sum += a * 2 ** (6-i)
    print(sum , end=' ')