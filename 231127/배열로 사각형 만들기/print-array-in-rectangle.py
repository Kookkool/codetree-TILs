answer=[
    [0 for _ in range(5)]
    for _ in range(5)
] 

for i in range(5):
    answer[0][i]=1

for r in range(1,5):
    for c in range(5):
        answer[r][c]=answer[r-1][c]+answer[r][c-1]

for r in range(5):
    for c in range(5):
        print(answer[r][c],end=' ')
    print()