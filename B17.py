import math
n = int(input())
h = list(map(int, input().split()))
dp = [math.inf] *n
dp[0] = 0

for i in range(n-1):
    if i < n-2:
        dp[i+2] = min(dp[i+2], dp[i] + abs(h[i]-h[i+2]))
    dp[i+1] = min(dp[i+1], dp[i]+abs(h[i] - h[i+1]))
l = [n]
pos = n-1
while True:
    if pos == 0:
        break
    if dp[pos] - dp[pos-1] == abs(h[pos] - h[pos-1]):
        pos -= 1
    else:
        pos -= 2
    
    l.append(pos+1)
print(len(l))
print(*reversed(l))