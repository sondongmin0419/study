def solution(info, query):
    answer = [0] * len(query)
    li_li_li = [[[[[] for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]


    def play (p_s):
        if p_s == 'cpp':
            return 1
        elif p_s == 'java':
            return 2
        elif p_s == 'python':
            return 3
        elif p_s == 'backend':
            return 1
        elif p_s == 'frontend':
            return 2
        elif p_s == 'junior':
            return 1
        elif p_s == 'senior':
            return 2
        elif p_s == 'chicken':
            return 1
        elif p_s == 'pizza':
            return 2
        elif p_s == '-':
            return 4
        else:
            return int(p_s)

    for i in range(len(info)):
        i_stack = []
        s = ''
        for j in range(len(info[i])):
            if info[i][j] != ' ':
                s += info[i][j]
            else:
                i_stack.append(play(s))
                s = ''
            if j == len(info[i]) - 1:
                i_stack.append(play(s))
        a1 = i_stack[3]
        b2 = i_stack[2]
        c3 = i_stack[1]
        d4 = i_stack[0]
        li_li_li[d4][c3][b2][a1].append(i_stack[4])

    def make_li(n):
        if n == 4:
            return [1,2,3]
        else:
            return [n]

    def cal(a, b, c, d, f):
        total = 0
        li_a = make_li(a)
        li_b = make_li(b)
        li_c = make_li(c)
        li_d = make_li(d)
        for a_ in li_a:
            for b_ in li_b:
                for c_ in li_c:
                    for d_ in li_d:
                        for score in li_li_li[d_][c_][b_][a_]:
                            if score >= f:
                                total += 1
        return total


    for j in range(len(query)):
        i_stack = []
        s = ''
        for i in range(len(query[j])):
            if query[j][i] != ' ':
                s += query[j][i]
            else:
                if s != 'and':
                    i_stack.append(play(s))
                s = ''
            if i == len(query[j]) - 1:
                i_stack.append(play(s))
        a1 = i_stack[3]
        b2 = i_stack[2]
        c3 = i_stack[1]
        d4 = i_stack[0]
        answer[j] = cal(a1, b2, c3, d4, i_stack[4])

    return answer


a = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]

print(solution(a, b))