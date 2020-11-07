def m_sort(nums):
    if len(nums) < 2:
        return nums
    center = len(nums)//2
    left, right = nums[:center], nums[center:]
    return play(m_sort(left), m_sort(right))


def play(l_li, r_li):
    global cnt
    if l_li[-1] > r_li[-1]:
        cnt += 1
    result = []
    l_i = r_i = 0
    while l_i != len(l_li) and r_i != len(r_li):
        if l_li[l_i] < r_li[r_i]:
            result.append(l_li[l_i])
            l_i += 1
        elif l_li[l_i] > r_li[r_i]:
            result.append(r_li[r_i])
            r_i += 1
        else:
            result.append(l_li[l_i])
            result.append(r_li[r_i])
            l_i += 1
            r_i += 1
    result.extend(l_li[l_i:])
    result.extend(r_li[r_i:])
    return result


T = int(input())

for TC in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    print('#%d %d %d' % (TC, m_sort(li)[N//2], cnt))
