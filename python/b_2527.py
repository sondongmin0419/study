for TC in range(4):

    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        p1, p2 = p2, p1
        q1, q2 = q2, q1

    result = 'a'

    if p1 < x2 or q1 < y2 or q2 < y1:
        result = 'd'
    elif (p1 == x2 and y1 == q2) or (p1 == x2 and y2 == q1):
        result = 'c'
    elif (p1 == x2 and (y2 <= y1 <= q2 or y1 <= y2 <= q1)) or ((y1 == q2 or y2 == q1) and (x1 <= x2 <= p1)):
        result = 'b'

    print(result)