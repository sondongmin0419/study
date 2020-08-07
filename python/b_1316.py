n = int(input())

total = 0
for i in range(n):           #테스트 케이스
    s = input()
    set_li = set({s[0]})
    for j in range(len(s)-1):            #문자전체 순회
        if s[j] != s[j+1]:
            if s[j+1] not in set_li:
                set_li.add(s[j+1])
            else:
                total += 1
                break
print(n - total)