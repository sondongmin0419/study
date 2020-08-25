li = [1, 2, 3, 4, 5]

def game (li):
    li[1:3] = li[2:0:-1]
    print(li)
    # li = [1, 3, 2, 4, 5]
    game(li)

game(li)