def solution(new_id):
    new_id = new_id.lower()
    result = ''
    i = 0
    while i < len(new_id):
        if 'a' <= new_id[i] <= 'z' or '0' <= new_id[i] <= '9' or new_id[i] == '-' or new_id[i] == '_':
            result += new_id[i]
        elif new_id[i] == '.':
            if i > 0 and (new_id[i - 1] == '.' or (len(result) > 0 and result[-1] == '.')):
                pass
            else:
                result += new_id[i]
        i += 1
    if len(result) != 0 and result[0] == '.':
        result = result[1:]
    if len(result) != 0 and result[-1] == '.':
        result = result[0:len(result) - 1]
    if not result:
        result = 'a'
    if len(result) > 15:
        result = result[:15]
        if len(result) != 0 and result[0] == '.':
            result = result[1:]
        if len(result) != 0 and result[-1] == '.':
            result = result[0:len(result) - 1]
    while len(result) < 3:
        result += result[-1]
    return result
