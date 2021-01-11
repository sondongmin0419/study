def solution(numbers):
    answer = []

    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            sum_ij = numbers[i] + numbers[j]
            if sum_ij in answer:
                pass
            else:
                answer.append(sum_ij)
    answer.sort()
    return answer