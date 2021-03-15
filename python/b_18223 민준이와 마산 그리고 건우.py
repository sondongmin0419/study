def t(n,l):
    global min_len
    if min_len < l:
        return
    visited[n] = 1
    for i in dict_node[n]:
        n_n = i[0]
        n_l = l+[1]
        if n_n == V:
            if min_len > n_l:
                min_len = n_l
        li.append([n_n,n_l])
    return


V, E, P = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(E)]

visited = [0]*5001
li = []
result = []
dict_node = {}
min_len = 10000*10000


for node in arr:
    if dict_node[node[0]]:
        dict_node[node[0]].append([node[1],node[2]])
    else:
        dict_node[node[0]] = [[node[1],node[2]]]

    if dict_node[node[1]]:
        dict_node[node[1]].append([node[0],node[2]])
    else:
        dict_node[node[1]] = [[node[0],node[2]]]

visited[1] = 1

t([1,0])
while True:
    for i in li:


