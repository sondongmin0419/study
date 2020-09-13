def solution(new_id):
    new_id = new_id.lower()
    i = 0
    li_id = list(new_id)
    result = []
    while True:
        if 'a' <= li_id[i] <= 'z' or li_id[i] == '.' or li_id[i] == '-' or li_id[i] == '_' or '0' <= li_id[i] <= '9':

            if result and result[-1] == '.' and li_id[i] == '.':
                pass
            else:
                result.append(li_id[i])
        else:
            pass
        i += 1
        if i >= len(li_id):
            break
    if result and result[0] == '.':
        result.pop(0)
    if result and result[len(result)-1] == '.':
        result.pop()
    if not result:
        result.append('a')
    while len(result) > 16:
        result.pop()
    if result and result[-1] == '.':
        result.pop()
    if len(result) <= 2:
        last = result.pop()
        while len(result) <= 2:
            result.append(last)
    answer = ''.join(result)
    return answer



print(solution(input()))