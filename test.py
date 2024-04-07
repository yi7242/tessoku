h, w = map(int, input().split())
l = [[] for i in range(h)]
s = [0, 0, 0]
for i in range(h):
    ll = list(input())
    for j in ll:
        l[i].append([j, -1])
    if "S" in ll:
        s[0] = i
        s[1] = ll.index("S")
n = int(input())
for i in range(n):
    r, c, e = map(int, input().split())
    l[r - 1][c - 1][1] = e

seen = [[False for i in range(w)] for j in range(h)]
from collections import deque

next = deque()
next.append(s)
all = {".", "#", "S", "T"}
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# print(l)


def search(done, hito, huta, nextcount):
    # print(done, hito, huta, nextcount)
    if hito == h - 1 and huta == w - 1:
        print("Yes")
        exit()
    for i in range(4):
        nowhito = hito + dx[i]
        nowhuta = huta + dy[i]
        if 0 <= nowhito < h and 0 <= nowhuta < w:
            if not (nowhito, nowhuta) in done:
                if l[nowhito][nowhuta] == snuke[nextnextcount]:
                    search(done | {(nowhito, nowhuta)}, nowhito, nowhuta, nextnextcount)


search(set(), 0, 0, 0)


print("No")
