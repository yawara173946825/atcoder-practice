X1, Y1, R1 = map(float, input().split())
X2, Y2, R2 = map(float, input().split())

d = (((X1 - X2) ** 2 + (Y1 - Y2) ** 2) ** 0.5)

if abs(R1 - R2) > d:
    Answer = 1
elif abs(R1 - R2) == d:
    Answer = 2
elif R1 + R2 > d:
    Answer = 3
elif R1 + R2 == d:
    Answer = 4
else:    
    Answer = 5

print(str(Answer))