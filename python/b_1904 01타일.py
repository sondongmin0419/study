N = int(input())

if N == 1:
    print(1)
else:
    before_1 = 1
    before_2 = 1
    for i in range(2, N + 1):
        result = (before_2 + before_1) % 15746
        before_2 = before_1
        before_1 = result

    print(result)
