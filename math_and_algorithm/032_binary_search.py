N, X = map(int,input().split())
A = list(map(int, input().split()))

if A.count(X) > 0:
    print("Yes")
else:
    print("No")