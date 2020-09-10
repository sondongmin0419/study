import sys
sys.stdin = open("input_5178.txt", "r")


class Tree:
    def __init__(self, N):
        self.li = [0] * (N + 1)
        self.N = N

    def put(self, num1, num2):
        self.li[num1] = num2

    def search_leaf(self, node):
        if node * 2 > N:
            self.sum += self.li[node]
        else:
            self.search_leaf(node * 2)
            if node * 2 != N:
                self.search_leaf(node * 2 + 1)
    def my_result(self, L):
        self.sum = 0
        self.search_leaf(L)
        return self.sum


T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = Tree(N)
    for _ in range(M):
        num1, num2 = map(int, input().split())
        tree.put(num1, num2)
    print('#%d %d'%(test_case, tree.my_result(L)))
