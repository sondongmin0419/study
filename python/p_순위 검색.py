from collections import defaultdict


def solution(info, query):
    dic = defaultdict(list)
    answer = []
    for i in range(len(info)):
        word = ''
        score = ''
        for j in range(len(info[i])):
            if 'a' <= info[i][j] <= 'z' or '-' and not ' ':
                word += info[i][j]
            else:
                score+= info[i][j]
        dic[word].append(int(score))

    result = []
    for i in range(len(query)):
        word = ''
        score = ''
        for j in range(len(info[i])):
            if 'a' <= info[i][j] <= 'z' or '-' and not ' ':
                word += info[i][j]
            elif '0' <= info[i][j] <= '9':
                score += info[i][j]
        cnt = 0
        for j in range(len(dic[word])):
            if dic[word][j] >= int(score):
                cnt += 1
        result.append(cnt)



    return result

a=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(a,b))