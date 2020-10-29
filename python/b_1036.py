def change(change_li):
    sum_ = 0
    for num in li:
        for j in range(len(num)-1, -1, -1):
            if ord(num[j]) < 65:
                if num[j] in change_li:
                    sum_ += (ord('Z') - 55) * 36 ** (len(num)-1-j)
                else:
                    sum_ += int(num[j]) * 36 ** (len(num)-1-j)
            else:
                if num[j] in change_li:
                    sum_ += (ord('Z') - 55) * 36 ** (len(num)-1-j)
                else:
                    sum_ += (ord(num[j])-55) * 36 ** (len(num)-1-j)
    return sum_


N = int(input())

li = []
set_ch = set()
li_ch = []
for i in range(N):
    li.append(input())
    for j in range(len(li[i])):
        set_ch.add(li[i][j])

li_ch = list(set_ch)
len_li_ch = len(li_ch)
K = int(input())
max_num = 0
cnt = 0

li_alpa_sum = [0] * len_li_ch
for i in range(len_li_ch):
    li_alpa_sum[i] = change(li_ch[i])

li_alpa_maxlist = []
for i in range(min(K, len_li_ch)):

    ind = li_alpa_sum.index(max(li_alpa_sum))

    if li_alpa_sum[ind] == -1:
        break
    li_alpa_maxlist.append(ind)
    li_alpa_sum[ind] = -1

for i in range(len(li_alpa_maxlist)):
    li_alpa_maxlist[i] = li_ch[li_alpa_maxlist[i]]

max_num = change(li_alpa_maxlist)
result_stack = []

while max_num > 0:
    result_stack.append(max_num % 36)
    max_num = max_num // 36
re = []

for i in range(len(result_stack)-1, -1, -1):
    if result_stack[i] > 9:
        re.append(chr((result_stack[i]+55)))
    else:
        re.append(str(result_stack[i]))

if not re:
    print(0)
else:
    print(''.join(re))
