N = int(input())
P = [None] * (N+1)
A = [None] * (N+1)
for i in range(1,N+1):
    P[i], A[i] = map(int,input().split())
    
dp = [ [ None ] * (N+1) for _ in range(N+1)]
dp[1][N] = 0
 
for LEN in reversed(range(0,N-1)):
    for l in range(1,N-LEN+1):
        r = l+LEN
        
        score1 = 0
        score2 = 0
        if l>=2 and l<=P[l-1]<=r:
            score1 = A[l-1]
            
        if r<=N-1 and l<=P[r+1]<=r:
            score2 = A[r+1]
        
        if l==1:
            dp[l][r] = dp[l][r+1]+score2
        elif r==N:
            dp[l][r] = dp[l-1][r]+score1
        else:
            dp[l][r] = max(dp[l-1][r]+score1,dp[l][r+1]+score2)
        
ans = 0
for i in range(1,N+1):
    ans = max(ans,dp[i][i])
    
print(ans)