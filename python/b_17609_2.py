T = int(input())

for TC in range(T):
    st = list(input())
    st_rev = st[::-1]          #문자열 reverse
    if st == st_rev:   #회문판별
        print(0)
    else:   # 회문아닐경우


        i = 0
        while i <= len(st) // 2:   # i가 0부터 문자열길이의 절반까지만 조회
            if st[i] != st_rev[i]:  # 문자열과 reverse한 문자열을 차레로 비교하며 다를경우
                if st[i+1:len(st)//2+1] == st_rev[i:len(st)//2]: # 기존문자열 i+1인덱스부터 (절반+1)까지 인덱스와
                    print(1)                                   #reverse한 문자열 그대로 비교해서
                    break
                elif st[i:len(st)//2] == st_rev[i+1:len(st)//2+1]: #기존 문자열 그대로와 reverse한 문자열 i+1부터비교
                    print(1)
                    break
                else:
                    print(2)
                    break
            i += 1
