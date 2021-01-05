N = int(input())

A = list(map(int, input().split()))

result = [A[0]]
m = 0
for i in range(1, N):
    if result[m] < A[i]:
        if len(result) > m + 1:
            result[m + 1] = A[i]
        else:
            result.insert(m + 1, A[i])
        m += 1
    else:
        if result[-1] > A[i]:
            result.append(A[i])
        else:
            for k in range(m, len(result)):
                if result[k] <= A[i]:
                    result[k] = A[i]
                    break
        for j in range(m+1):
            if result[j] >= A[i]:
                result[j] = A[i]
                break

print(len(result))
