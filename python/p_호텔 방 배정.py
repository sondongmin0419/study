from collections import defaultdict

def solution(k, room_number):
    answer = []
    visited = defaultdict(int)
    for i in range(len(room_number)):
        j = room_number[i]
        while True:
            if not visited.get(j):
                answer.append(j)
                visited[room_number[i]] = j
                visited[j] = j
                break
            else:
                j = visited[j]+1

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
