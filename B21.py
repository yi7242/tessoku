import math

n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))
b = []
for x in a:
    cc = 0
    for i in range(n):
        if x[i] == 1:
            cc += 2**i
    b.append(cc)
# print(b)
dp = [[math.inf for i in range(2**n)] for j in range(m + 1)]
dp[0][0] = 0
for i in range(m):
    for j in range(2**n):
        dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
        v = j | b[i]
        # print(i, j, v)
        dp[i + 1][v] = min(dp[i + 1][v], dp[i][j] + 1)
ans = dp[m][2**n - 1]
if ans == math.inf:
    print(-1)
else:
    print(ans)
