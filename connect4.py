"""
FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)
"""
import random
import os

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")


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
    if enter in valid_inputs: # for valid inputs
        return enter
    else: # invalid input
        print("Invalid input, please try again.")
        return validate_input(prompt, valid_inputs) # run function to prompt user again


def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    # Implement your solution below
    board_row = 6 # num of rows
    board_col = 7 # num of cols
    board = [[0 for i in range(board_col)] for i in range(board_row)] # create array of 0's 
    return board


def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	# Implement your solution below
	board_row = 6
	board_col = 7
	# Board layout
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


def local_2_player_game():
	"""
	Defines the main application loop.
	User chooses a type of game to play or to exit.

	:return: None
	"""
	# Implement your solution below
	
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
			move = execute_player_turn(player, board)
			
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


def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.
	:return: None
	"""
	clear_screen()
	# Menu
	print("=============== Main Menu ===============")
	print("Welcome to Connect 4!")
	print("1. View Rules")
	print("2. Play a local 2 player game")
	print("3. Play a game against the computer")
	print("4. Exit")
	print("=========================================")

	# Choosing an option
	user_input = validate_input("Please select an option (1, 2, 3, 4): ", ["1", "2", "3", "4"])
	
	if user_input == "1": # Rules
		clear_screen()
		print_rules() 
		home_input = validate_input("Please select an option (home, exit): ", ["home", "exit"])
		if home_input == "home": # back to main menu
			main()
		elif home_input == "exit": # exit
			exit()
	elif user_input == "2": # Local 2 player game
		clear_screen()
		local_2_player_game()
	elif user_input == "3": # Play CPU
		clear_screen() 
		game_against_cpu()
	elif user_input == "4": # Exit
		clear_screen()
		exit()

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
		random_column = random.randint(1, 7) # random number between 1 and 7
		if drop_piece(board, player, random_column):
			return random_column


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
	opponent = 0
	if player == 1:
		opponent = 2
	else:
		opponent = 1

	player_move = -1
	opponent_move = -1

	# Testing for possible win or loss
	for i in range(7):
		new_board = [row[:] for row in board] # new board to simulate possible wins or losses
		if drop_piece(new_board, player, i + 1) == True:
			new_board = [row[:] for row in board]
			row_index = 6
			for row in (new_board):
				row_index -= 1
				if new_board[row_index][i] == 0:
					new_board[row_index][i] = player
					if end_of_game(new_board) == player:
						new_board = [row[:] for row in board]
						drop_piece(board, player, i + 1)
						return i + 1

					else:
						new_board =  [row[:] for row in board]
						new_board[row_index][i] = opponent
						if end_of_game(new_board) == opponent:
							if opponent_move == -1:
								opponent_move = i + 1


	cpu_move = -1
	cpu_move = opponent_move

	# if no move to block or win 
	while cpu_move == -1:
		rand = random.randrange(1,8) # random place to drop
		if drop_piece(board, player, rand) == True:
			cpu_move = rand
			return rand

	drop_piece(board, player, cpu_move)
	return cpu_move


def cpu_player_hard(board, player):
	"""
	Executes a move for the CPU on hard difficulty.
	This function creates a copy of the board to simulate moves.
	<Insert player strategy here>

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError


def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""
	cpu_input = validate_input("Please select an option (easy, medium, hard): ", ["easy", "medium", "hard"])

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
			
			if player % 2 == 1: # human player
				move = execute_player_turn(player, board)
			else: # CPU move depending on difficulty
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


if __name__ == "__main__":
	board = create_board()
	main()

print("test")
