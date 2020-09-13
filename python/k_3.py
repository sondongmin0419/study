def solution(info, query):
    li_info = []
    li_query = []
    answer = [0] * len(query)

    for i in range(len(info)):
        i_stack = []
        stack = []
        d_num = 0
        for j in range(len(info[i])):
            if info[i][j] != ' ':
                stack.append(info[i][j])
            else:
                i_stack.append(''.join(stack))
                stack = []
            if j == len(info[i]) - 1:
                i_stack.append(''.join(stack))
        li_info.append(i_stack)

    for j in range(len(query)):
        i_stack = []
        stack = []
        for i in range(len(query[j])):
            if query[j][i] != ' ':
                stack.append(query[j][i])
            else:
                s = ''.join(stack)
                if s != 'and':
                    i_stack.append(''.join(stack))
                stack = []
            if i == len(query[j]) - 1:
                i_stack.append(''.join(stack))
        li_query.append(i_stack)
        for i in range(len(li_info)):
            if li_info[i][0] == li_query[j][0] or li_query[j][0] == '-':
                if li_info[i][1] == li_query[j][1] or li_query[j][1] == '-':
                    if li_info[i][2] == li_query[j][2] or li_query[j][2] == '-':
                        if li_info[i][3] == li_query[j][3] or li_query[j][3] == '-':
                            if int(li_info[i][4]) >= int(li_query[j][4]):
                                answer[j] += 1

    return answer


a = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]

solution(a, b)