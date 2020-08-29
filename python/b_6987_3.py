N = 6


def play():
    if len(v) == 15 and " ".join(v) not in result:
        result.add(" ".join(v))
        # print(result)
        v.pop()
        return 0

    for k in range(3):
        if li_c[k] == 1:
            v.append('1')
            play()
        elif li_c[k] == 0:
            v.append('0')
            play()
        elif li_c[k] == -1:
            v.append('-1')
            play()
    v.pop()

li = [[0, 0, 0] for _ in range(6)]

li_c = [1, 0, -1]
v = []
result = set()
#  ab ac ad ae af bc bd be bf cd ce cf de df ef

#승 무 패
play()
print(result)
