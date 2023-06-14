import math

n,w = map(int, input().split())
weight = []
value = []

for i in range(n):
    x,y = map(int, input().split())
    weight.append(x)
    value.append(y)

dp = [[math.inf for i in range(100009)]for j in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(100009):
        if dp[i][j] == math.inf:
            continue
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        dp[i+1][j+value[i]] = min(dp[i+1][j+value[i]], dp[i][j] + weight[i])
for i in range(100000, 1, -1):
    if dp[n][i] <= w:
        print(i)
        exit()