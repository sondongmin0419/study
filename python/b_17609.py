T = int(input())

for TC in range(T):
    st = input()
    li_st = list(st)
    len_st = len(st)
    status = True
    result = 0
    result_l = 0
    result_r = 0
    while status:
        result = 0
        result_l = 0
        result_r = 0

        i = 0
        if len_st % 2 == 0:   # asd dsa
            while len_st//2 >= i:
                if li_st[i] != li_st[-i-1]:
                    if not status:
                        result = 1
                        break
                    elif li_st[len_st//2-2] == li_st[len_st//2]:
                        del (li_st[-i-1])
                        status = False
                        continue
                    elif li_st[len_st//2-1] == li_st[len_st//2+1]:
                        del (li_st[i])
                        status = False
                        continue
                    else:
                        result = 1
                        status = False
                        break
                i += 1
        else:
            while len_st//2 >= i:  # asdfg gfddsaa
                if li_st[i] != li_st[-i-1]:
                    if not status:
                        result = 1
                        break
                    elif li_st[len_st//2-1] == li_st[len_st//2]:
                        del (li_st[-i-1])
                        status = False
                        continue
                    elif li_st[len_st//2] == li_st[len_st//2+1]:
                        del (li_st[i])
                        status = False
                        continue
                    else:          abb b bba x
                        result = 1
                        status = False
                        break
                i += 1
        if status:
            print(0)
            break
        elif result == 0:
            print(1)
            break
        else:
            print(2)
            break