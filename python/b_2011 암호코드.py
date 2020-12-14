num = input()

li = [0] * (len(num) + 1)
li[0] = 1
li[1] = 1
if num[0] == '0':
    print(0)
else:
    for i in range(2, len(num)+1):
        if '0' < num[i-1]:
            li[i] += (li[i-1])
        n = int(num[i-2]) * 10 + int(num[i-1])
        if 10 <= n <= 26:
            li[i] += (li[i-2] )

    print(li[-1]% 1000000)

