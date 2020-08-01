num = input()

copy_num = num
cnt = 0

# while(True):
#     if int(copy_num) == 1:
#         cnt = 60
#         break
#     if int(copy_num) < 10:
#         copy_num = '0' + copy_num

#     sum_num = int(copy_num[0]) + int(copy_num[1])
#     new_num = (copy_num[1])+str(sum_num%10)
#     cnt += 1
#     if num == new_num:
#         break
#     else:
#         copy_num = new_num
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

