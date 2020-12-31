import sys


def a_():
    if sum(arr_2)==0:
        test_li = stack[:]
        a_li.append(test_li)
    for i in range(4):
        if arr_2[i] >0:
            arr_2[i] -= 1
            stack.append(a[i])
            a_()
            arr_2[i]+=1
            stack.pop()




input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().rstrip().split()))
arr_2 = list(map(int, input().rstrip().split()))
a = ['+', '-', '*', '/']

stack = []
a_li = []
a_()
result = []

max_result = -1000000000
min_result = 1000000000
for cal in a_li:
    total = arr[0]
    for i in range(N-1):
        if cal[i] == '+':
            total += arr[i+1]
        elif cal[i] == '-':
            total -= arr[i+1]
        elif cal[i] == '*':
            total *= arr[i+1]
        else:
            if total >=0:
                total //= arr[i+1]
            else:
                total = -((-total)//arr[i+1])
    if total > max_result:
        max_result = total
    if total < min_result:
        min_result = total



print(max_result)
print(min_result)