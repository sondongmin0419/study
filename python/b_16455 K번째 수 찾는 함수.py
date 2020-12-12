def kth(a: list, k: int):
    s = 0
    e = len(a) - 1
    while True:
        i = s
        j = e
        while True:
            while i <= e and a[i] <= a[s]:
                i += 1
            while a[j] > a[s]:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[s], a[j] = a[j], a[s]
        if j == k - 1:
            return a[k-1]
        elif j < k-1:
            s = j + 1
        else:
            e = j - 1

# kth([3,5,7,8,1,2], 2)