ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))

# 成分を求める
BAx, BAy = ax - bx, ay - by
BCx, BCy = cx - bx, cy - by
CAx, CAy = ax - cx, ay - cy
CBx, CBy = bx - cx, by - cy

# 内積を求める
if BAx * BCx + BAy * BCy < 0:
    pattern = 1
elif CAx * CBx + CAy * CBy < 0:
    pattern = 2
else:
    pattern = 3

if pattern == 1:
    Answer = (BAx **2 + BAy ** 2) ** 0.5
if pattern == 2:
    Answer = (CAx ** 2 + CAy ** 2) ** 0.5
if pattern == 3:
    # BAとBC
    P = abs(BAx * BCy - BAy * BCx)
    B = (BCx ** 2 + BCy ** 2) ** 0.5
    Answer = P / B

print(Answer)