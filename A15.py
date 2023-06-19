import math
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [math.inf] * n
for i in range(n-1):
    if i < n-2:
        dp[i+2] = min(dp[i+2], dp[i] + b[i])
    dp[i+1] = min(dp[i+1], dp[i]+a[i])
print(dp)