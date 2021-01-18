def solution(n):
    hanoi(n, 1, 3, 2)
    return answer


def hanoi(n, h_from, h_to, h_):
    if n == 1:
        answer.append([h_from, h_to])
        return

    hanoi(n - 1, h_from, h_, h_to)
    answer.append([h_from, h_to])
    hanoi(n - 1, h_, h_to, h_from)

answer = []
