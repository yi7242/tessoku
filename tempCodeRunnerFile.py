import math

n,w = map(int, input().split())
weight = []
value = []

for i in range(n):
    x,y = map(int, input().split())
    weight.append(x)
    value.append(y)

dp = [[-1 for i in range(w+1)]for j in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(w+1):
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        if j + weight[i] <= w:
            dp[i+1][j+weight[i]] = max(dp[i+1][j+weight[i]], dp[i][j] + value[i])
print(max(dp[n]))