def end_of_game(board): # Question 6
	"""
	Checks if the game has ended with a winner
	or a draw.

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""
	# Implement your solution below
	#raise NotImplementedError
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

	

	#function to check the status of game
	def check_game_status(board, possibilities):
		for row in board:
			splice_int1 = 0
			splice_int2 = 4
			for i in range(possibilities):
				if 0 in row[splice_int1:splice_int2]:
					splice_int1 += 1
					splice_int2 += 1
					pass
				elif 1 in row[splice_int1:splice_int2] and 2 in row[splice_int1:splice_int2]:
					splice_int1 += 1
					splice_int2 += 1
					pass
				else:
					print(row[splice_int1:splice_int2][0])

	#check horizontal wins 
	check_game_status(board, 4)

	#check vertical wins 
	check_game_status(vert_board, 3)
	return