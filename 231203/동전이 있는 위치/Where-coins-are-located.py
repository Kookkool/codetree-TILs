n,m=tuple(map(int,input().split()))

matrix=[
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(m):
    r,c=tuple(map(int,input().split()))
    matrix[r-1][c-1]=1


for a in range(n):
    for b in range(n):
        print(matrix[a][b],end=' ')
    print()