import math

def solution(w,h):

    cnt = 0
    answer = 0
    if h>w:
        for i in range(1,w):
            cnt += h - math.ceil(i*h/w)
        answer = cnt*2
    elif h == w:
        answer = w*h - w
    else:
        for i in range(1,h):
            cnt += w - math.ceil(i*w/h)
        answer = cnt*2




    return answer



print(solution(2,2))