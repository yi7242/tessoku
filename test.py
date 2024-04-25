h, w = map(int, input().split())
<<<<<<< HEAD
a = []
start = [0, 0]
end = [0, 0]
for i in range(h):
    a.append(list(input()))
for i in range(h):
    for j in range(w):
        if a[i][j] == "S":
            start[0] = i
            start[1] = j
        if a[i][j] == "T":
            end[0] = i
            end[1] = j
n = int(input())
medic = [[-1 for i in range(w)] for j in range(h)]
rs = []
cs = []
es = []
for i in range(n):
    r, c, e = map(int, input().split())
    medic[r - 1][c - 1] = i  # 後でes番目を参照するようにする
    rs.append(r - 1)
    cs.append(c - 1)
    es.append(e)
=======
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
>>>>>>> 665ff57821b44e920f420543fba69874b3a46e5e
from collections import deque
import math

<<<<<<< HEAD
n += 2
rs.append(start[0])
cs.append(start[1])
es.append(0)
rs.append(end[0])
cs.append(end[1])
es.append(0)

reachable = [[False for _ in range(n)] for j in range(n)]  # [n-2] == "S" [n-1] == "T"
print(a)
for i in range(n):
    dist = [[math.inf for j in range(w)] for k in range(h)]
    dist[rs[i]][cs[i]] = 0
    q = deque()
    q.append((rs[i], cs[i], es[i]))
    while q:
        x, y, energy = q.popleft()
        if energy > 0:
            for px, py in [(0, -1), (0, 1), (1, 0), (1, -1)]:
                nx, ny = x + px, y + py
                if 0 <= nx <= h - 1 and 0 <= ny <= w - 1:
                    print(nx, ny)
                    if a[nx][ny] != "#":
                        ne = energy - 1
                        if medic[nx][ny] != -1:
                            reachable[i][medic[nx][ny]] = True
                            ne = max(ne, es[medic[nx][ny]])
                        if a[nx][ny] == "S":
                            reachable[i][n - 2] = True
                        if a[nx][ny] == "T":
                            reachable[i][n - 1] = True

                        if ne > dist[nx][ny]:
                            dist[nx][ny] = ne
                            q.append(nx, ny, ne)
    print(dist)
    print(reachable)
=======
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
>>>>>>> 665ff57821b44e920f420543fba69874b3a46e5e
