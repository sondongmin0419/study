T = int(input())

for TC in range(1, T+1):
    n = int(input())
    s = input()
    check = 0
    if s[0:4] == '2020' or s[n-4:n] == '2020':
        check = 1
    if s[0:3] == '202' and s[n-1:n] == '0':
        check = 1
    if s[0:2] == '20' and s[n-2:n] == '20':
        check = 1
    if s[0:1] == '2' and s[n-3:n] == '020':
        check = 1
    if check == 1:
        print('YES')
    else:
        print('NO')