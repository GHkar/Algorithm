S = str(input())

tag = False
word = []
ans = []
for i in range(len(S)) :
    if S[i] == '>' :
        word.append(S[i])
        ans.append("".join(word))
        word = []
        tag = False
        continue

    if i == len(S) - 1 : 
        word.append(S[i])
        ans.append("".join(word[::-1]))
        word = []
        continue

    if tag == False and S[i] == ' ':
        ans.append("".join(word[::-1]))
        word = []
        continue

    if S[i] == '<' :
        tag = True
        if len(word) > 0:
            ans.append("".join(word[::-1]))
            word = []
            word.append(S[i])
            continue

    word.append(S[i])


real_ans = []
for i in range(len(ans)) :
    if ans[i][0] != '<' and ans[i-1][0] != '<' and i != 0 : 
        real_ans.append(" ")

    real_ans.append(ans[i])

print("".join(real_ans))

