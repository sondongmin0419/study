import sys


def play(name):
    for key in p_li[name]:
        if key not in visited:
            visited.append(key)


T = int(sys.stdin.readline())

for TC in range(1, T+1):
    F = int(input())
    p_li = {}
    for _ in range(F):
        p1, p2 = sys.stdin.readline().split()

        if p1 not in p_li:
            p_li[p1] = {p2}
        else:
            p_li[p1].add(p2)

        if p2 not in p_li:
            p_li[p2] = {p1}

        else:
            p_li[p2].add(p1)

        visited = [p1, p2]
        cnt = 0
        while True:
            play(visited[cnt])
            cnt += 1
            if cnt == len(visited):
                break

        print(cnt)
