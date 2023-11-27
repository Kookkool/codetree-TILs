n=int(input())

answer=[
    [0 for _ in range(n)]
    for _ in range(n)
]

for r in range(n):
    answer[0][r]=1
    answer[r][0]=1

for rr in range(1,n):
    for c in range(1,n):
        answer[rr][c]=answer[rr-1][c]+answer[rr][c-1]+answer[rr-1][c-1]


for r in range(n):
    for c in range(n):
        print(answer[r][c],end=' ')
    print()