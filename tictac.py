def winCheck(board):
    for i in range(3):
        if len(set(board[i*3:i*3+3])) is  1 and board[i*3] is not 'c': return True
    
    for i in range(3):
       if (board[i] is board[i+3]) and (board[i] is  board[i+6]) and board[i] is not 'c':
           return True
    
    if board[0] is board[4] and board[4] is board[8] and board[4] is not 'c':
        return  True
    if board[2] is board[4] and board[4] is board[6] and board[4] is not 'c':
        return  True
    return False

def nextMove(player,board) :
	nextPlayer = 'o' if player == 'x' else 'x'
	if len(set(board)) == 1: return 0,4
	print(len(board),"len")
	if winCheck(board)	:
		if(player == "x") :
			return -1,-1
		else :
			return 1,-1
	list_empty_spaces = []
	list_scores= []
	c = board.count('c')
	if c is 0:
		return 0,-1
	num_blanks = board.count("c")
	for i in range(len(board)):
		print i
		if board[i] is 'c' :
			list_empty_spaces.append(i)

	for i in list_empty_spaces	:	
		board[i] = player
		ret,move=nextMove(nextPlayer,board)
		list_scores.append(ret)
		board[i]="c"

	if	player is "x" :
			maxele=max(list_scores)
			return maxele,list_empty_spaces[list_scores.index(maxele)]
	elif player is "o" :
			minele=min(list_scores)
			return minele,list_empty_spaces[list_scores.index(minele)]

f2 =open("./output.txt","w+")
f= open("./boards.txt","r")
for line in f:
	temp_board=list(line)
	temp_board.pop(9)
	print temp_board
	score,move=nextMove('x',temp_board)
	print move
	f2.write(str(move)+'\n')
f2.close()
f.close()
