import random

# Copy and paste any code from previous tasks here

def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty.
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	#creating another board that has its rows filled with the columns of the original board	
	vert_board= [0]*len(board[0])
	def verti_row(board, board_column_index):
		vert_row = [0]*len(board)
		row_column_index = -1
		for row in board:
			row_column_index += 1
			vert_row[row_column_index] = row[board_column_index]
		return vert_row
			
	column_index = -1
	for i in vert_board:
		column_index +=1
		vert_board[column_index] = verti_row(board, column_index)



		#creating another board that has its rows filled with the diagonals of the original board
	def diagonal_row(board, row_index, column_index):
		diag_row = ([-1]*len(board))#use -1 as empty lists containing 0 would give false results
		diag_index = -1 
		for row in board:
			if row_index <= len(board) - 1 and column_index <= len(board[0]) - 1:
				diag_index += 1
				diag_row[diag_index] = board[row_index][column_index]
				column_index += 1
				row_index += 1
			else:
				break
		return diag_row

	def diagonal_board(board):
		diag_board = [0] * (len(board) + (len(board[0]) - 1))
		column_index = 0
		row_index = len(board)
		for i in range(len(board) + (len(board[0]) - 1)):
			if row_index >= 1:
				row_index -= 1
			elif column_index <= (len(board[0]) - 1):
				column_index += 1
			diag_board[i] = diagonal_row(board, row_index, column_index)
		diag_brd = []
		diag_row = []
		a=0
		diag_board = diag_board[::-1]
		for i in reversed(diag_board):
			if -1 not in i:
				a=1
			if a == 1:
				diag_brd+=[i]
			else:
				while a == 0:
					for b in i:
						if b == -1:
							diag_row+=[-1]
					for c in i:
						if c != -1:
							diag_row+=[c]
					diag_brd+=[diag_row]
					diag_row = []
					break
		diag_board = diag_brd[::-1]
		return diag_board

	reversed_board = []
	for i in board:
		reversed_board+= [i[::-1]]


		
		#function to check the status of game by verifying spliced lists of all rows of the boards
	def check_game_status(board, possibilities, board_type):
		wins = []
		rows = 0
		row_num = 0
		for row in board:
			row_num+=1
			rows+=1
			splice_int1 = 0
			for i in range(possibilities+1):
				if 0 in row[splice_int1:(splice_int1+3)] or -1 in row[splice_int1:(splice_int1+4)]:
					splice_int1 += 1
					pass
				elif 1 in row[splice_int1:(splice_int1+3)] and 2 in row[splice_int1:(splice_int1+4)]:
					splice_int1 += 1
					pass
				else:
					if 1 in row[splice_int1:(splice_int1+3)] or 2 in row[splice_int1:(splice_int1+3)]:
						if splice_int1 == 0:
							if row[splice_int1+3] == 0:
								wins+=[[rows, splice_int1+4, board_type, row[splice_int1:(splice_int1+3)][0]]]
								splice_int1+=1
						elif splice_int1+2 == len(row) - 1:
							if row[splice_int1-1] == 0:
								wins+=[[rows, splice_int1, board_type, row[splice_int1:(splice_int1+3)][0]]]
								splice_int1+=1
						else:
							if row[splice_int1-1] == 0:
								wins+=[[rows, splice_int1, board_type, row[splice_int1:(splice_int1+3)][0]]]
								splice_int1+=1
							elif row[splice_int1+3] == 0:
								wins+=[[rows, splice_int1+4, board_type, row[splice_int1:(splice_int1+3)][0]]]
								splice_int1+=1
		return(wins)


	win = [check_game_status(board, 4,"horizontal"),check_game_status(vert_board, 3,"vertical"), check_game_status(diagonal_board(board), 3,"forwards_diagonal"), check_game_status(diagonal_board(reversed_board), 3,"backwards_diagonal")]
	#print(win)
	move_deciding = []
	for i in win:
		for b in i:
			if b[2] == 'vertical':
				c = []
				c+=[[b[1],b[0],b[3]]]
				move_deciding+=c
			elif b[2] == 'forwards_diagonal':
				d = []
				r = b[0]
				c = b[1]
				r -= (c - 1)
				r = len(board[0]) - (r - 1)
				rr = c
				cc = r
				d+=[[rr,cc,b[3]]]
				move_deciding+=d
			elif b[2] == "backwards_diagonal":
				d = []
				r = b[0]
				c = b[1]
				r -= (c - 1)
				rr = c
				cc = r
				d+=[[rr,cc,b[3]]]
				move_deciding+=d
			else:
				d=[]
				d+=[[b[0],b[1],b[3]]]
				move_deciding+=d
	#print(move_deciding)
	fin_move = []
	for i in move_deciding:
		if i[0]!=len(board):
			if board[i[0]][i[1]-1] != 0:
				fin_move+=[i]
		else:
			fin_move+=[i]
	cpu_move = -1
	for i in fin_move:
		if i[2] == player:
			return(i[1])
		else:
			cpu_move = i[2]
	return(cpu_move)

board = [
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 2, 0, 0, 0],
[1, 1, 0, 2, 0, 0, 0],
[1, 1, 0, 2, 2, 0, 2]]