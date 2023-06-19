from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

n,k,l = map(int, input().split())
tetsudou = [set() for i in range(n)]
df = UnionFind(n)

for i in range(k):
    p,q = map(int, input().split())
    df.union(p-1,q-1)
df2 = UnionFind(n)
for i in range(l):
    p,q = map(int, input().split())
    df2.union(p-1, q-1)
hoge = defaultdict(int)
for i in range(n):
    hoge[(df.find(i), df2.find(i))] += 1
for i in range(n):
    if i == n-1:
        print(hoge[(df.find(i), df2.find(i))])
    else:
        print(str(hoge[(df.find(i), df2.find(i))]) + " ", end="")