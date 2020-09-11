import sys
sys.stdin = open("input_3752.txt", "r")

T = int(input())

for TC in range(1, T+1):

    N = int(input())

    score_li = list(map(int, input().split()))
    score_max = sum(score_li)
    score_sum = [0] * (score_max+1)
    score_sum[0] = 1
    for j in range(N):
        for i in range(len(score_sum)-1,-1,-1):
            if score_sum[i] == 1:
                score_sum[i+score_li[j]] = 1

    print('#%d %d' % (TC, score_sum.count(1)))
