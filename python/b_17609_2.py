T = int(input())

for TC in range(T):
    st = list(input())
    st_rev = st[::-1]
    result = 1
    if st == st_rev:   #회문판별
        print(0)
        continue
    else:
        i = 0
        while i <= len(st) // 2:
            if st[i] != st_rev[i]:
                if st[i+1:len(st)//2+1] == st_rev[i:len(st)//2]:
                    result = 0
                    break
                elif st[i:len(st)//2] == st_rev[i+1:len(st)//2+1]:
                    result = 0
                    break
                else:
                    break
            i += 1
        if result == 0:
            print(1)
        else:
            print(2)