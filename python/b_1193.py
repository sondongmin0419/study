n = int(input())

i = 0
total = 0
while True:
    i += 1
    n = n - i
    if n > i+1:
        continue
    else:
        i += 1
        break
if i % 2 == 1:
    r = i
    c = 1
else:
    c = i
    r = 1

while n > 1:
    n -= 1
    if i % 2 == 1:
        r -= 1
        c += 1
    else:
        r += 1
        c -= 1

print(f'{r}/{c}')