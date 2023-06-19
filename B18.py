n,s = map(int, input().split())
a = list(map(int, input().split()))
dp = [[[] for i in range(s+1)] for j in range(n+1)]
dp[0][0] = [0]
for i in range(n):
    for j in range(s+1):
        if len(dp[i][j]) > 0:
            dp[i+1][j] = []
            for x in dp[i][j]:
                dp[i+1][j].append(x)
            if j+ a[i]  <= s:
                dp[i+1][j+a[i]] = []
                for x in dp[i][j]:
                    dp[i+1][j+a[i]].append(x)
                dp[i+1][j+a[i]].append(i+1)
if len(dp[n][s]) == 0:
    print(-1)
else:
    print(len(dp[n][s])-1)
    print(*dp[n][s][1:])