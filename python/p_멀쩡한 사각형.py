import math

def solution(w,h):

    k = math.ceil(h/w)
    answer = w*(h - k)


    return answer



print(solution(8,12))