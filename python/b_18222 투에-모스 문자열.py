k = int(input())

x = 1
x_n = 0
while True:
    if x < k:
        x *= 2
        x_n += 1
    else:
        break

n = 0
while 2**(x_n) > 2:
    print(2**(x_n), x_n, k, n)
    if (2 ** (x_n - 1)) < k:

        n_k = 2 ** (x_n) - k
        k = 2 ** (x_n - 1) - n_k
        n += 1
        x_n -= 1
    else:
        x_n -= 1

result = 0
print(k,n)


if k % 2 == 0:
    result = 1
else:
    result = 0

if n % 2 == 0:
    print(result)
else:
    print((result + 1) % 2)
