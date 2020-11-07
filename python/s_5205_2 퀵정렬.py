def Quick_sort(a):
    n=len(a)
    if n<=1: # 리스트가 1개면 정렬하지 않는다.
        return a
    pivot = a[-1] #리스트의 마지막을 피벗이라고 구함
    g_left=[] # 피벗 수보다 작은 수를 담을 리스트
    g_right=[] #피벗 수보다 큰 수를 담을 리스트
    for i in range(0,n-1):
        if a[i]<=pivot:
             g_left.append(a[i]) #리스트의 수가 피벗보다 작으면 g_left 에 추가
        else:
            g_right.append(a[i])
    return Quick_sort(g_left)+ [pivot] +Quick_sort(g_right)


T = int(input())

for TC in range(1, T+1):

    N = int(input())

    li = list(map(int, input().split()))
    print('#%d %d' % (TC, Quick_sort(li)[N//2]))

