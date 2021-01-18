from collections import defaultdict


def solution(n, m):
    max_n = 1
    i = 2
    n_ = n
    arr_n = defaultdict(int)
    arr_n[1] = 1
    while i <= n:
        if n_ % i == 0:
            arr_n[i] += 1
            n_ = n_ // i
            continue
        i += 1
    j = 2
    m_ = m
    arr_m = defaultdict(int)
    arr_m[1] = 1
    while j <= m:
        if m_ % j == 0:
            arr_m[j] += 1
            m_ = m_ // j
            continue
        j += 1

    for key, value in arr_n.items():
        if arr_m.get(key):
            max_n *= key ** min(value, arr_m.get(key))

    answer = [max_n, n * m // max_n]
    return answer

print(solution(2,5))