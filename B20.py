import math
s = input()
t = input()
sl = len(s)
tl = len(t)
dp = [[math.inf for j in range(tl+1)] for i in range(sl+1)]
for j in range(tl+1):
    dp[0][j] = j
for i in range(sl+1):
    dp[i][0] = i
for i in range(1, sl+1):
    for j in range(tl+1):
        # print(s[i-1], t[j-1])
        if j != 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
            if s[i-1] == t[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1)
        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
# print(dp)
print(dp[sl][tl])