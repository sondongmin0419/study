def cmp(s, t):
    if s == t:
        return 1
    else:
        return 0


T = int(input())

for TC in range(1, T+1):
    test = input()
    target = list(input())
    result = 0
    for i in range(len(target)-len(test)+1):
        result = cmp("".join(target[i:i+len(test)]), test)
        if result == 1:
            break
    print(f'#{TC} {result}')
