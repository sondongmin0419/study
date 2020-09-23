N = int(input())


def play():
    for i in range(min(li_a_len, li_b_len)):
        if li_a[i] > li_b[i]:
            return 'A'
        elif li_a[i] < li_b[i]:
            return 'B'
    if li_a_len > li_b_len:
        return 'A'
    elif li_a_len < li_b_len:
        return 'B'
    return 'D'


for i in range(N):
    li_a = list(map(int, input().split()))
    li_b = list(map(int, input().split()))
    li_a_len = li_a.pop(0)
    li_b_len = li_b.pop(0)
    li_a.sort(reverse=True)
    li_b.sort(reverse=True)
    result = play()
    print(result)
