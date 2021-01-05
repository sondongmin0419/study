word_1 = input()
word_2 = input()

dic = {}
for i in range(len(word_1)):
    if dic.get(word_1[i]):
        dic[word_1[i]].append(i)
    else:
        dic[word_1[i]] = [i]

result = []
for i in range(len(word_2)):
    if dic.get(word_2[i]):
        w = dic[word_2[i]]
        if i == 0:
            result.append(w)
        else:
            for ww in range(w):
                if result[-1] < ww:
                    result.append(ww)
                else:
                    for k in range(len(result)):
                        if result[k] >= ww:
                            result[k] = ww
                            break

print(len(result))