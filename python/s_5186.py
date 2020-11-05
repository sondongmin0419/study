T = int(input())

for TC in range(1, T+1):
    num = float(input())
    li = []
    n = 0
    for i in range(1,13):
        k = 2 ** -i
        if num >= k:
            num -= k
            li.append('1')
        else:
            li.append('0')
        if num == 0:
            break
    if num != 0:
        result = 'overflow'
        print('#%d %s'%(TC, result))
    else:
        print('#%d %s' %(TC, ''.join(li)))