n = int(input())
cnt = 0
for i in range(1,n+1):
    if 1 <= i <= 99:
        cnt += 1
        continue
    elif i == 1000:
        continue
    n_str = str(i)
    if int(n_str[2]) - int(n_str[1]) == int(n_str[1]) - int(n_str[0]):
        cnt += 1

print(cnt)

