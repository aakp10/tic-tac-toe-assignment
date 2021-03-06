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

def generateBoard(board,index,fboard):
	if index!=9 :
		for i in range(3):
			if i==0 :
				board[index]='x'
				fboard.write(str(board))
				fboard.write("\n")
				indexa=index
				indexa=indexa+1
				generateBoard(board,indexa,fboard)				
			elif i==1 :
				board[index]='o'
				fboard.write(str(board))
				fboard.write("\n")
				indexb=index
				indexb=indexb+1
				generateBoard(board,indexb,fboard)
			else :
				board[index]='c'
				fboard.write(str(board))
				fboard.write("\n")
				indexc=index
				indexc=indexc+1
				generateBoard(board,indexc,fboard)
	else :
		return 0

def checkValidity(board):
	if board.count("x") != board.count("o")	:
		f2.write("invalid \n")
		return 0
	if winCheck(board):
		f2.write("has won \n")
		return 0
	return 1

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



board=list("ccccccccc")
fboard = open("./allBoards.txt","w+")
generateBoard(board,0,fboard)
fboard.close()

f2 =open("./output.txt","w+")
f= open("./allBoards.txt","r")


for line in f:
	temp_board=[]
	input_from_file=[]
	input_from_file=line
	print input_from_file
	print len(input_from_file)
	for i in range(len(input_from_file)):
		if input_from_file[i] is 'x' or input_from_file[i] is 'o' or input_from_file[i] is 'c'	:
			temp_board.append(input_from_file[i])
	print len(temp_board)
	print temp_board

	if checkValidity(temp_board)==0:
		continue
	score,move=nextMove('x',temp_board)
	print move
	f2.write(str(move)+'\n')

f2.close()
f.close()

