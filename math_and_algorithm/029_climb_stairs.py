N = int(input())

dp = [0] * (N + 1)
dp[0] = 1

# 1段目に行くには1通りしかない
dp[1] = 1

# 2段目より上に行く場合、一段で飛ばした場合と、2段で飛ばした場合の2通りある

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])