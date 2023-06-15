s = input()
t = input()
sl = len(s)
tl = len(t)
dp = [[0 for i in range(sl+1)] for j in range(tl+1)]
for i in range(tl+1):
    for j in range(sl+1):
        if i != 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j])
        if j != 0:
            dp[i][j] = max(dp[i][j-1], dp[i][j])
        if i!= 0 and j!=0 and t[i-1] ==s[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+ 1)
print(dp[tl][sl])