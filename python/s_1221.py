T = int(input())

test = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV':5,
        'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
text_n = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV',
        6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
for TC in range(1,T+1):

    tc = list(input().split())
    tc_len = int(tc[1])
    li = list(input().split())
    li_n = [0] * tc_len
    for i in range(tc_len):
        li_n[i] = test[li[i]]
    li_n.sort()
    print(f'#{TC}')
    for i in li_n:
        print(text_n[i], end=' ')
    print()