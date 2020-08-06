T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(A)
li_a = []

for i in range(1 << n):
    total = 0
    cnt = 0
    for j in range(n + 1):
        if i & (1 << j):
            total += A[j]
            cnt += 1
    dic_a = {}
    dic_a[total] = cnt
    li_a.append(dic_a)

for TC in range(1, T+1):
#     A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
    N, K = map(int, input().split())
#
#     n = len(A)
#
    # result = 0
    # for i in range(1 << n):
#         total = 0
#         cnt = 0
#         for j in range(n+1):
#             if i & (1 << j):
#                 total += A[j]
#                 cnt += 1
#         if total == K and cnt == N:
#             result += 1
    result = 0
    for dic in li_a:
        for key, value in dic.items():
            if key == K and value == N:
                result += 1

    print(f'#{TC} {result}')

