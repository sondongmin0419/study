import sys
sys.stdin = open("input_5177.txt", "r")


class Tree:
    def __init__(self):
        self.li = [0]

    def sort(self, num):
        if num >= 2:
            if self.li[num] < self.li[num // 2]:
                self.li[num], self.li[num // 2] = self.li[num // 2], self.li[num]
                self.sort(num // 2)

    def append(self, data):
        num = len(self.li)
        self.li.append(data)
        self.sort(num)

    def my_sum(self, node):
        if node <= 1:
            return self.li[node]
        else:
            return self.li[node] + self.my_sum(node // 2)

    def my_result(self):
        last = len(self.li) - 1
        self.sum = 0
        if last >= 2:
            return self.my_sum(last // 2)
        else:
            return 0


T = int(input())

for TC in range(1, 1 + T):
    N = int(input())
    tree = Tree()
    for i in map(int, input().split()):
        tree.append(i)
    print('#%d %d'% (TC, tree.my_result()))