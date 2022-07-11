# 폴리오미노

board = list(input())

board.append('.')
count = 0

for j in range(len(board)) :
    if board[j] == 'X' : 
        count += 1

    else:
        if count == 0 : continue
        # 짝수인지
        if count % 2 == 0 :
            remain = count % 4
            for i in range(count - remain) :
                board[j- count + i] = 'A'
            for i in range(count, count - remain, -1) :
                board[j- count + i -1] = 'B'
        else :
            print(-1)
            quit()
        
        count = 0



for i in range(len(board) - 1) :
    print(board[i], end="")

