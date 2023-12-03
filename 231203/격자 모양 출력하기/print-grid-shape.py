n,m = tuple(map(int,input().split()))

matrix=[
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(m):
    r,c=tuple(map(int,input().split()))
    matrix[r-1][c-1]=r*c

for rr in range(n):
    for cc in range(n):
        print(matrix[rr][cc],end=' ')
    print()