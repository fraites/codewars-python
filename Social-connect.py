import random
from time import process_time


# Social network connectivity problem
# Given social network containing n members
# & log file containing m timestamps when members formed friendships
# determine time when all members are connected
# friendship is equivalence relationship ( if x.root = y.root )

class UnionFind:

    def __init__(self, n):
        self.members = [member for member in range(n)]
        self.size = [1] * n
        self.count_connect = n

    def base(self, mem):
        i = mem
        while i != self.members[i]:
            self.members[i] = self.members[self.members[i]]
            i = self.members[i]
        return i

    def find(self, mem1, mem2):
        return self.base(mem1) == self.base(mem2)

    def connect(self, mem1, mem2):
        i = self.base(mem1)
        j = self.base(mem2)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.members[i] = self.members[j]
            self.size[j] += self.size[i]
        else:
            self.members[j] = self.members[i]
            self.size[i] += self.size[j]
        self.count_connect -= 1


def connect_friends():
    t = process_time()
    number = 10
    social_network = UnionFind(number)
    rand_mem1 = 0
    rand_mem2 = 0
    while social_network.count_connect != 1:
        rand_mem1 = random.randint(0, number-1)
        rand_mem2 = random.randint(0, number-1)
        if not social_network.find(rand_mem1, rand_mem2):
            social_network.connect(rand_mem1, rand_mem2)
    for i in range(1, number):
        if social_network.members[i] != social_network.members[i-1]:
            social_network.count_connect += 1
            social_network.connect(i, i-1)
    elapsed_time = process_time() - t
    print(elapsed_time)
    
