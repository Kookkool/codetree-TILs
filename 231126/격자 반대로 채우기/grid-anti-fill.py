n=int(input())
answer=[
    [0 for _ in range(n)]
    for _ in range(n)
]

count=1

for start_col in range(n-1,-1,-1):
    if (n-1-start_col)%2==0:
        
        for curr_row in range(n-1,-1,-1):
            answer[curr_row][start_col]=count
            count+=1

    else :
        for curr_row in range(n):
        
            answer[curr_row][start_col]=count
            count+=1

for r in range(n):
    for c in range(n):
        print(answer[r][c],end =' ')
    print()