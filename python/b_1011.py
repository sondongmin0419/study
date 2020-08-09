# def total(n):
#     return (2 * 1 + (n - 1)) * n // 2
#
#
# def space(len_xy, i, cnt):
#     cnt += 1
#     len_xy -= i
#     if len_xy >= total(i + 1):
#         return space(len_xy, i + 1, cnt)
#     elif len_xy == 2 or len_xy == 1:
#         return space(len_xy, 1, cnt)
#     elif len_xy == 0:
#         return cnt
#     elif len_xy >= total(i):
#         return space(len_xy, i, cnt)
#     elif len_xy < total(i):
#         return space(len_xy, i - 1, cnt)
#
#
# T = int(input())
#
# for TC in range(1, T + 1):
#     x, y = map(int, input().split())
#     len_fxy = y - x
#     count = 0
#     start = 1
#     result = space(len_fxy, start, count)
#     print(result)
T = int(input())

for TC in range(1, T+1):
    x, y = map(int, input().split())

    count = 1
    while True:
        if count**2 <= y-x < (count+1)**2:
            break
        count += 1
    if count**2 == y-x:
        print(count*2 - 1)
    elif count**2 <= y-x <= count**2 + count:
        print(count*2)
    else:
        print(count*2+1)