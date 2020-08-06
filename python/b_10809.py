n = input()

for i in range(ord('a'),ord('z')+1):
    s = chr(i)
    print(n.find(s),end=' ')
    # print(chr(i))
