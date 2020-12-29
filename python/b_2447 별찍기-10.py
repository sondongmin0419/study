def b_2447(n,x,y):
    if n == 1:
        arr[y][x] ='*'

    else:
        n = n//3
        for dy in range(3):
            for dx in range(3):
                if dy != 1 or dx != 1:
                    b_2447(n,x+dx*n,y+dy*n)

    return


n = int(input())

arr = [list(' ' for _ in range(n)) for _ in range(n)]

b_2447(n,0,0)

for k in arr:
    print(''.join(k))