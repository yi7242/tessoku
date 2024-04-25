h, w = map(int, input().split())
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
from collections import deque
import math

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
