import math

n, wmax = map(int, input().split())
w, v = [0] * n, [0] * n
for i in range(n):
    w[i], v[i] = map(int, input().split())
dp = [[math.inf for i in range(1009)] for j in range(n + 1)]
