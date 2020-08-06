a, b = map(str, input().split())
n_a = ''
n_b = ''
for n in range(len(a)-1,-1,-1):
    n_a += a[n]
    
for n in range(len(b)-1,-1,-1):
    n_b += b[n]

max_n = n_b

if n_a > n_b:
    max_n = n_a


print(max_n)