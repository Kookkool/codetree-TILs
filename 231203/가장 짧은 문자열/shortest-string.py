w1=input()
w2=input()
w3=input()

w1_len=len(w1)
w2_len=len(w2)
w3_len=len(w3)

mx = max([w1_len, w2_len, w3_len])
mn = min([w1_len, w2_len, w3_len])

print(mx - mn)