w1=input()
w2=input()
w3=input()

w1_len=len(w1)
w2_len=len(w2)
w3_len=len(w3)


if w1_len>w2_len:
    if w1_len>w3_len:
        max_word=w1
        if w2_len>w3_len:
            min_word=w3
        else:
            min_word=w2
    else:
        max_word=w3
        min_word=w2
else:
    if w2_len>w3_len:
        max_word=w2
        min_word=w1
    else:
        max_word=w3
        min_word=w1

print(len(max_word)-len(min_word))