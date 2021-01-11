def solution(a):
    if len(a) < 2:
        return 0
    result_n = [0] * len(a)
    result_limit = [-1] * len(a)
    for i in range(len(a)):
        if i > 0 and result_limit[a[i]] < i - 1:
            result_limit[a[i]] = i
            result_n[a[i]] += 1
        elif i != (len(a) - 1) and a[i] != a[i + 1]:
            result_limit[a[i]] = i + 1
            result_n[a[i]] += 1
        else:
            result_limit[a[i]] = i

    answer = max(result_n) * 2

    return answer

