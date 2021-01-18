from collections import defaultdict


def solution(n, works):
    arr_w = defaultdict(int)
    for work in works:
        arr_w[work] += 1
    max_work = max(arr_w)

    while n > 0:
        if arr_w.get(max_work) <= n:
            arr_w[max_work - 1] += arr_w.get(max_work)
            n -= arr_w.get(max_work)
            del (arr_w[max_work])
        elif n < arr_w.get(max_work):
            arr_w[max_work - 1] += n
            arr_w[max_work] -= n
            n =0

        if n == 0:
            break
        max_work-=1
        if max_work <= 0:
            break

    answer = 0
    for work, value in arr_w.items():
        answer += value * work ** 2

    return answer

print(solution(1,[2,1,2]))