num = input()
cnt = 0

num2 = int(num)
num3 = num2
while(True):
    a = num2 // 10
    b = num2 % 10
    s_num = a + b
    n_num = b*10 + s_num%10
    cnt += 1
    if num3 == n_num:
        break
    else:
        num2 = n_num


print(cnt)

