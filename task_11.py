def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    # Iterate through each row from bottom up
    for row in reversed(board):
        # Drop player token in the lowest free space
        # Check for valid column input
        if column < 1 or column > 7:
            return False
        # Array index start at 0, but humans count from 1, so minus one from input column account for that
        if row[column - 1] == 0:
            row[column - 1] = player
            return True

    # If all spaces are filled (no 0s)
    return False

def end_of_game(board):
	"""
	Checks if the game has ended with a winner
	or a draw.

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""

	# * Win Check
	def win(string):
		if "1111" in string:
			return 1
		elif "2222" in string:
			return 2

	# * Rows -> Strings
	for row in board:
		row_str = "".join([str(i) for i in row])
		# If there's a win return the winner
		exists = win(row_str)
		if exists:
			return exists
	
	# To check for draw further down
	filled_slots = True
	# * Columns -> Strings
	for i in range(len(board[0])):  # Length of each row in original board
		column_str = ""
		# Concatenate elements of ith index from each row into a string
		for row in board:
			column_str += str(row[i])
			# If empty spaces then won't be a draw
			if row[i] == 0:
				filled_slots = False
		exists = win(column_str)
		if exists:
			return exists

	# * Diagonals -> Strings
	def diagonal_check(board):
		for col in range(3, len(board[0])):  # 3-6
			# Second half from right-most column down
			if col == 6:
				for row in range(3):  # 0-2
					diagonal_str = ""
					i = row
					j = col
					while i < col and j >= row:
						diagonal_str += str(board[i][j])
						i += 1
						j -= 1
					exists = win(diagonal_str)
					if exists:
						return exists
			# First half from left most relevant column
			else:
				diagonal_str = ""
				row = 0
				i = row
				j = col
				# Do this until row and column number are switched
				while i <= col and j >= row:
					diagonal_str += str(board[i][j])
					i += 1
					j -= 1
				exists = win(diagonal_str)
				if exists:
					return exists

	# Diagonal /
	exists = diagonal_check(board)
	if exists:
		return exists  # Returning the value from win() to main
	# Diagonal \
	flipped_board = [row for row in reversed(board)]
	exists = diagonal_check(flipped_board)
	if exists:
		return exists

	# * Keep Playing or Draw
	if filled_slots:
			return 3  # All slots are filled so draw
	else:
		return 0  # There are empty slots left so keep playing
	
def cpu_player_hard(board, player):
	"""
	Executes a move for the CPU on hard difficulty.
	This function creates a copy of the board to simulate moves.
    
	<Insert player strategy here>

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: None
	"""

	PLAYER_TURN = 1
	CPU_TURN = 2
	# Takes the current board position with one new move and calculates static evaluation of that move
	def score_position(board, game_status):
		if game_status != 0:
			if game_status == 2: # CPU winning move
				return 1000
			elif game_status == 1: # Player winning move
				return -1000
			else: # Draw
				return 0	
		
		# TODO: Strategy to evaluate the score (likelihood to win) of a current position

	def minimax(board, depth, is_cpu_move):
		game_status = end_of_game(board)
		if depth == 0 or game_status != 0:
			return score_position(board, game_status)
		if is_cpu_move:
			max_score = -1000
			for col_value, col_index in enumerate(board[0]):
				if col_value != 0: # If the first row of the board if not empty the board is filled
					continue
				new_board = [row for row in board]
				drop_piece(new_board, col_index + 1, CPU_TURN)
				score = minimax(new_board, depth - 1, False) # Computes the score for the player move 
				max_score = max(score, max_score)
		else: # Player move 
			min_score = 1000	
			for col_value, col_index in enumerate(board[0]):
				if col_value != 0: # If the first row of the board if not empty the board is filled
					continue
				new_board = [row for row in board]
				drop_piece(new_board, col_index + 1, PLAYER_TURN)
				score = minimax(new_board, depth - 1, True) # Computes the score for the player move 
				min_score = min(score, min_score)
				
