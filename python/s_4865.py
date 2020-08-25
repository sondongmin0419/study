import sys
sys.stdin = open("sample_input (2).txt", "r")


T = int(input())

for TC in range(1, T+1):
    cnt = {}
    max_cnt = 0
    test = set(input())
    target = list(input())
    for i in range(len(target)):
        if target[i] in test:
            if target[i] in cnt:
                cnt[target[i]] += 1
            else:
                cnt[target[i]] = 1
            if max_cnt < cnt[target[i]]:
                max_cnt = cnt[target[i]]

    print(f'#{TC} {max_cnt}')


