def make_str(num_list):
    s = ""
    for i in num_list:
        s += str(i)
    return s


def partial_reverse(num_list, n):
    for i in range(K//2):
        num_list[n+i], num_list[n+K-i-1] = num_list[n+K-i-1], num_list[n+i]
    return num_list


def solve(s):
    queue = []
    visited[make_str(s)] = 1
    queue.append(s)
    ans = sorted(s)

    cnt = -1
    while len(queue) != 0:
        qsize = len(queue)
        cnt += 1
        for _ in range(qsize):
            cur = queue.pop(0)
            if cur == ans:
                return cnt
            for i in range(N - K + 1):
                copied = cur[:]
                partial_reverse(copied, i)
                key = make_str(copied)
                if key in visited:
                    continue
                visited[key] = 1
                queue.append(copied)
    return -1


N, K = map(int, input().split())
seq = list(map(int, input().split()))
visited = {}

print(solve(seq))
