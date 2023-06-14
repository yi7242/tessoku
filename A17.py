import math
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [math.inf] * n
dp[0] = 0
for i in range(n-1):
    if i < n-2:
        dp[i+2] = min(dp[i+2], dp[i] + b[i])
    dp[i+1] = min(dp[i+1], dp[i] + a[i])
place = n-1
l = [n]
while place != 0:
    if dp[place] - dp[place-1] == a[place-1]:
        l.append(place)
        place = place-1
    else:
        l.append(place-1)
        place = place-2
print(len(l))
print(*reversed(l))
