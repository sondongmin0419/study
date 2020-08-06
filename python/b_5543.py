price = [0]*5

min_buger = 2000
min_juice = 2000
for i in range(3):
    price[i] = int(input())
    if price[i] < min_buger:
        min_buger = price[i]

for i in range(3,5):
    price[i] = int(input())
    if price[i] < min_juice:
        min_juice = price[i]
result = min_buger+min_juice-50

print(result) 