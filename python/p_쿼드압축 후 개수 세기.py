def solution(arr):
    answer = [0,0]
    n = len(arr)
    p = 1
    for i in range(n):
        for j in range(n):
            answer[arr[i][j]] += 1
    p = 2
    while p <= n:
        for y in range(0,n,p):
            for x in range(0,n,p):
                total = 0
                for j in range(y,y+p):
                    for k in range(x,x+p):
                        total += arr[j][k]
                if total == p*p:
                    answer[1] -= 3
                elif total == 0:
                    answer[0] -= 3
        p *= 2

    return answer

arr = [list(map(int, input().split())) for _ in range(4)]
print(solution(arr))