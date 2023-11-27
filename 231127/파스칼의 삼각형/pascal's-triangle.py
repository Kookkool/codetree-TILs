n=int(input())

answer=[]
for i in range(1,n+1):
    a=[]
    for z in range(i):
        a.append(1)
    answer.append(a)

for r in range(n):
    for c in range(1,r):
        answer[r][c]=answer[r-1][c-1]+answer[r-1][c]


for r in range(n):
    for c in range(r+1):
        print(answer[r][c],end=' ')
    print()