n = int(input())

i = 0
cnt = 0
while True:
    n = n - i*6
    if n <= 1:
        break
    else:
        i += 1
        continue
print(i+1)