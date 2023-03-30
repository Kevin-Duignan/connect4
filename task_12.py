import random
def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    # Implement your solution below
    print(prompt, end="")
    enter = input()
    if enter in valid_inputs:
        return enter
    else:
        print("Invalid input, please try again.")
        return validate_input(prompt, valid_inputs)


# Copy and paste create_board here
def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    # Implement your solution below
    board_row = 6
    board_col = 7
    board = [[0 for i in range(board_col)] for i in range(board_row)]
    return board

# Copy and paste print_board here
def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	# Implement your solution below
	board_row = 6
	board_col = 7
	print("========== Connect4 =========")
	print("Player 1: X       Player 2: O\n")
	print("  1   2   3   4   5   6   7")
	print(" --- --- --- --- --- --- ---")
	for row in range(board_row):
		print("|", end = "")
		for col in range(board_col):
			if board[row][col] == 1:
				print(" X |", end = "")
			elif board[row][col] == 2:
				print(" O |", end = "")
			elif board[row][col] == 0:
				print("   |", end = "")
		print("\n --- --- --- --- --- --- ---")
	print("=============================")
	
# Copy and paste drop_piece here
import random

# Copy and paste drop_piece here
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
	if 1 <= column <= 7:
		for row in reversed(board):
			# Drop player token in the lowest free space
			if row[column - 1] == 0:
				row[column - 1] = player
				return True

	# If all spaces are filled (no 0s)
	return False

# Copy and paste execute_player_turn here
def execute_player_turn(player, board):  # Task 5
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    while True:
        column = int(input(f"Player {player}, please enter the column you would like to drop your piece into: "))
        # drop_piece returns true if there is space
        if drop_piece(board, player, column):
            return column
        else:
            print("Invalid turn, please try again.")
			
# Copy and paste end_of_game here
def end_of_game(board):  # Question 6 - Rohit
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # Implement your solution below

    # creating another board that has its rows filled with the columns of the original board
    vert_board = [0] * len(board[0])

    def verti_row(board, board_column_index):
        vert_row = [0] * len(board)
        row_column_index = -1
        for row in board:
            row_column_index += 1
            vert_row[row_column_index] = row[board_column_index]
        return vert_row

    column_index = -1
    for i in vert_board:
        column_index += 1
        vert_board[column_index] = verti_row(board, column_index)

    # creating another board that has its rows filled with the diagonals of the original board
    def diagonal_row(board, row_index, column_index):
        diag_row = ([3] * len(board))
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
        return diag_board

    reversed_board = [0] * len(board)
    index = 0
    for i in board:
        reversed_board[index] = i[::-1]
        index += 1

    # function to check the status of game by verifying spliced lists of all rows of the boards
    def check_game_status(board, possibilities):
        game_status = 0
        game_can_continue = -1
        for row in board:
            splice_int1 = 0
            for i in range(possibilities):
                if 0 in row[splice_int1:(splice_int1 + 4)] and 1 not in row[
                                                                        splice_int1:(splice_int1 + 4)] and 2 not in row[
                                                                                                                    splice_int1:(
                                                                                                                            splice_int1 + 4)] and 3 not in row[
                                                                                                                                                           splice_int1:(
                                                                                                                                                                   splice_int1 + 4)]:
                    game_can_continue = 0
                if 0 in row[splice_int1:(splice_int1 + 4)] or 3 in row[splice_int1:(splice_int1 + 4)]:
                    splice_int1 += 1
                    pass
                elif 1 in row[splice_int1:(splice_int1 + 4)] and 2 in row[splice_int1:(splice_int1 + 4)]:
                    splice_int1 += 1
                    pass
                else:
                    game_status = row[splice_int1:(splice_int1 + 4)][0]
        return ([game_status, game_can_continue])

        # function to check the status of game by verifying spliced lists of all rows of the boards
    def check_game_status(board, possibilities):
        game_status = 0
        game_can_continue = -1
        for row in board:
            splice_int1 = 0
            for i in range(possibilities):
                if 0 in row[splice_int1:(splice_int1 + 4)]:
                    game_can_continue = 0
                if 0 in row[splice_int1:(splice_int1 + 4)] or 3 in row[splice_int1:(splice_int1 + 4)]:
                    splice_int1 += 1
                    pass
                elif 1 in row[splice_int1:(splice_int1 + 4)] and 2 in row[splice_int1:(splice_int1 + 4)]:
                    splice_int1 += 1
                    pass
                else:
                    game_status = row[splice_int1:(splice_int1 + 4)][0]
        return ([game_status, game_can_continue])

    # check horizontal wins
    # print(check_game_status(board, 4))
    # check horizontal wins
    # print(check_game_status(board, 4))
    # check vertical wins
    # print(check_game_status(vert_board, 3))

    # check diagonal wins
    # forwards_diagonal
    # print(check_game_status(diagonal_board(board), 3))

    # backwards_diagonal
    # print(check_game_status(diagonal_board(reversed_board), 3))

    # computing final status of game
    final_result = 0
    if check_game_status(board, 4)[0] != 0:
        final_result = check_game_status(board, 4)[0]
    elif check_game_status(vert_board, 3)[0] != 0:
        final_result = check_game_status(vert_board, 3)[0]
    elif check_game_status(diagonal_board(board), 3)[0] != 0:
        final_result = check_game_status(diagonal_board(board), 3)[0]
    elif check_game_status(diagonal_board(reversed_board), 3)[0] != 0:
        final_result = check_game_status(diagonal_board(reversed_board), 3)[0]
    else:
        if check_game_status(board, 4)[1] == 0 and check_game_status(vert_board, 3)[1] == 0 and \
                check_game_status(diagonal_board(board), 3)[1] == 0 and \
                check_game_status(diagonal_board(reversed_board), 3)[0] == 0:
            pass
        else:
            final_result = 3

    return final_result

# Copy and paste cpu_player_easy
def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	while True:
		random_column = random.randint(1, 7)
		if drop_piece(board, player, random_column):
			return random_column

# Copy and paste cpu_player_medium
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
			cpu_move = i[1]

	while cpu_move == -1:
		rand = random.randrange(1,8)
		if drop_piece(board, player, rand) == True:
			cpu_move = rand

	return(cpu_move)
# Copy and paste cpu_player_hard


def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	import os
	os.system('cls' if os.name == 'nt' else 'clear')
	

def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""
	cpu_input = validate_input("Please select an option (easy, medium, hard): ", ["easy", "medium", "hard"])
	#if cpu_input == "easy":
		#cpu_player_easy(board, player)
	#elif cpu_input == "medium":
		#cpu_player_medium(board, player)
	#elif cpu_input == "hard":
		#cpu_player_hard(board, player)


	turn_counter = 0

	# Do While
	while True:
		clear_screen()
		print_board(board)
		# If start of game
		if turn_counter == 0:
			# Player 1 starts
			print("Your turn to start, Player 1!")
			move = execute_player_turn(1, board)
			turn_counter += 1
			game_status = end_of_game(board)
		
		# Else if in the middle of a game	
		elif game_status == 0:
			# Compute player turn
			player = (turn_counter % 2) + 1 # Even turn is p1, odd turn is p2
			previous_player = ((turn_counter - 1) % 2) + 1 # Last turn
			
			# Previous move and prompt for next move
			print(f"Player {previous_player}'s turn was column {move}.")
			if player % 2 == 1:
				move = execute_player_turn(player, board)
			else:
				if cpu_input == "easy":
					move = cpu_player_easy(board, player)
				elif cpu_input == "medium":
					move = cpu_player_medium(board, player)
				elif cpu_input == "hard":
					move = cpu_player_hard(board, player)
				
			turn_counter += 1
			game_status = end_of_game(board)
		
		# If game is over
		else:
			break

	# When game has ended
	if game_status == 3:
		print("It's a draw!")
	else:
		# execute_player_turn returns player number if that player wins
		print(f"Player {game_status} wins!")
		

board = create_board()

if __name__ == "__main__":
	# Enter test code below

	game_against_cpu()