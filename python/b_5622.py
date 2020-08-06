st = input()

result = ''
for i in st:
    if i in ['A', 'B', 'C']:
        result += '2'
    elif i in ['D', 'E', 'F']:
        result += '3'
    elif i in ['G', 'H', 'I']:
        result += '4'
    elif i in ['J', 'K', 'L']:
        result += '5'
    elif i in ['M', 'N', 'O']:
        result += '6'
    elif i in ['P', 'Q', 'R', 'S']:
        result += '7'
    elif i in ['T', 'U', 'V']:
        result += '8'
    elif i in ['W', 'X', 'Y', 'Z']:
        result += '9'

total = 0

for i in result:
    total += int(i) + 1


print(total)