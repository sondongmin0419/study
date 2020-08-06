
n = 1

li = list(range(1,10001))

while(n<=10000):

    total = 0
    a = n // 1000
    b = n // 100 - a * 10
    c = n // 10 - a * 100 - b* 10
    d = n %10
    total = n + a + b + c + d
    if total in li:
        li.remove(total)
    n += 1

for i in li:
    print(i)