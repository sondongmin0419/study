def f1(n,g,K,m):
    global cnt
    global minV

    cnt += 1
    if n==g:
        if M>=K and minV>m-K:
            minV = m-K
    elif m>= K and minV <= m-K:
        return
    else:
        f1(n+1, g, K, m)
        f1(n+1, g, K, m+H[n])


def f(n, g, K):
    global minV
    if 