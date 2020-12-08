N, K = map(int, input().split())

li = list(map(int, input().split()))

result = 10**6

for i in range(K,len(li)+1):
    for j in range(len(li)-i+1):
        m = sum(li[j:j+i])/i
        v = 0
        for a in li[j:j+i]:
            v += (a-m)**2
        v = v/i
        f = v**(0.5)
        if f < result:
            result = f

print(result)