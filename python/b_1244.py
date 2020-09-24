N = int(input())
switch = [0]
switch.extend(list(map(int, input().split())))

student_n = int(input())

for i in range(student_n):

    s, n = map(int, input().split())
    if s == 1:
        k = 1
        while True:
            switch[k*n] = (switch[k*n] + 1) % 2
            k += 1
            if k*n > N:
                break
    elif s == 2:
        k = 1
        switch[n] = (switch[n] + 1) % 2
        while True:
            if 0 < n-k <= N and 0 < n+k <= N and switch[n-k] == switch[n+k]:
                switch[n+k] = (switch[n+k] + 1) % 2
                switch[n-k] = (switch[n-k] + 1) % 2
            else:
                break
            k += 1

for i in range(1, N+1):
    if i % 20 != 0:
        print(switch[i], end=' ')
    else:
        print(switch[i])
