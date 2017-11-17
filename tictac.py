def isWin(board):
	for i in range(3):
		if len(set(board[i*3:i*3+3])) is 1 and board[i*3] !='c' :
			return True
	for i in range(3):
		if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] != 'c':
			return True
	if board[0] == board[4] and board[4] == board[8] :
		return True
	elif board[2] == board[4] and board[4] == board[6] :
		return True
	return False

def nextMove(player,board) :
	nextPlayer = 'o' if player == 'x' else 'x'

	print(len(board),"len")
	if isWin(board)	:
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
"""
def test():
    assert isWin(list("XXXccc000"))==True
    #assert nextMove(list('ccccccccc'),'X') == (0,4)
    print nextMove(list('XX000cX0c'),'X') == (0,5)
    assert nextMove(list('00cXXOcX0'),'X') == (0,2)
    assert nextMove(list('XXc00cX0c'),'0') ==(-1,5)
    assert nextMove(list('XXcc0cX00'),'0') ==(1,2) # no chance for O to win
	#return "Test cases passed"




temp_board=['X','X','c','0','0','c','X','0','c']
print nextMove('0',temp_board)
temp_board=['X','X','c','c','0','c','X','0','0']
print nextMove('0',temp_board)
temp_board=['X','X','0','0','0','c','X','0','c']
print nextMove('X',temp_board)
temp_board=['X','X','0','0','0','c','X','0','c']
print nextMove('X',temp_board)

temp_board=['X' ,list('XXcc0cX00')]
print nextMove('X',temp_board)

temp_board=['0','0','c','X','X','0','c','X','0']
print nextMove('X',temp_board)
"""
f2 =open("./output.txt","w+")
f= open("./boards.txt","r")
for line in f:
	temp_board=[]
	for c in line:
		temp_board.append(c)
	temp_board.pop(9)
	print temp_board
	score,move=nextMove('x',temp_board)
	print move
	f2.write(str(move)+'\n')
f2.close()
f.close()
