def solution(orders, course):
    c_len = len(course)
    test_dic = {}
    count_li = [0] * c_len
    for i in range(len(orders)):
        test = list(orders[i])
        for j in range(1, 1 << len(test)):
            stack = []
            for k in range(len(test)):
                if j & (1 << k):
                    stack.append(test[len(test)-k-1])
            stack.sort()
            test_str = ''.join(stack)
            if test_str in test_dic:
                test_dic[test_str] += 1
            else:
                test_dic[test_str] = 1
            for c_l in range(c_len):
                if course[c_l] == len(test_str):
                    if count_li[c_l] < test_dic[test_str]:
                        count_li[c_l] = test_dic[test_str]
    answer = []

    for key, value in test_dic.items():
        for c_l in range(c_len):
            if course[c_l] == len(key) and value == count_li[c_l] and value>1:
                answer.append(key)
    answer.sort()
    print(answer)
    return answer


a = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
b = [2,3,5]
solution(a, b)