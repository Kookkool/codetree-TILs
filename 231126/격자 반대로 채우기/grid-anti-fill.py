n=int(input())
answer=[
    [0 for _ in range(n)]
    for _ in range(n)
]

count=1
for start_col in range(n-1,-1,-1):
    curr_col=start_col
   
    if start_col%2!=0:
        curr_row=n-1
        while 0<=curr_col and curr_row >= 0:
            answer[curr_row][curr_col]=count

            curr_row-=1
            count+=1

    else :
        curr_row=0
        while 0<=curr_col and curr_row < n:
            answer[curr_row][curr_col]=count

            curr_row+=1
            count+=1
   
for r in range(n):
    for c in range(n):
        print(answer[r][c],end =' ')
    print()