N, W = map(int, input().split())
w = [0] * N
v = [0] * N

for i in range(0, N):
    w[i], v[i] = map(int, input().split())

# アイテムiまで見た時、容量Wに詰められる最大価値
# 列に重さ、行に品物の個数の二次元配列
dp = [[0] * (W + 1) for i in range(N + 1)]

# 個数i
for i in range(1, N+1):
    # 重さj
    for j in range(0, W+1):
        if j < w[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            # 選ばない場合と選んだ場合の大きいほうを選択
            # 重さjから、選ぶ場合の数を引いた部分の値をプラスする
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])

print(dp[N][W])