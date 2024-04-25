<<<<<<< HEAD
import math

n, wmax = map(int, input().split())
w, v = [0] * n, [0] * n
for i in range(n):
    w[i], v[i] = map(int, input().split())
dp = [[math.inf for i in range(1009)] for j in range(n + 1)]
=======
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

# seen = [[False for i in range(w)] for j in range(h)]
from collections import deque

next = deque()
next.append(s)
all = {".", "#", "S", "T"}
dx = [0, 0, 1, -1]
neededEnergy = [[-1] * w for i in range(h)]
dy = [1, -1, 0, 0]
# print(l)
while len(next) != 0:
    now = next.popleft()
    # print(now)
    x = now[0]
    y = now[1]
    energy = now[2]
    # done = now[3]
    # seen[x][y] = True
    energy = max(energy, l[x][y][1])
    if l[x][y][0] == "T":
        print("Yes")
        exit()
    if energy <= 0:
        continue
    neededEnergy[x][y] = max(neededEnergy[x][y], energy)
    for i in range(4):
        ni = x + dx[i]
        nj = y + dy[i]
        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue
        # if seen[ni][nj]:
        # if (ni, nj) in done:
        #     continue
        if l[ni][nj] == "#":
            continue
        if neededEnergy[ni][nj] >= (energy - 1):
            continue
        next.append([ni, nj, energy - 1])
print("No")
>>>>>>> 665ff57821b44e920f420543fba69874b3a46e5e
