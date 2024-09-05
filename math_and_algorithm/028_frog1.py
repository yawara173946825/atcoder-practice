N = int(input())
H = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
for i in range(1,N):
    if i == 1:
        dp[i] = abs(H[i-1] - H[i])
    if i >= 2:
        v1 = dp[i-1] + H[i-1] - H[i]
        v2 = dp[i-2] + H[i-2] - H[i]
        dp[i] = min(v1,v2)

print(dp[N-1])
    
