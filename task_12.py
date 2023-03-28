# Copy and paste create_board here

# Copy and paste print_board here

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

# Copy and paste end_of_game here

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
	clear_screen()
	cpu_input = validate_input("Please select an option (easy, medium, hard): ", ["easy", "medium", "hard"])
	if cpu_input == "easy":
		cpu_player_easy(board, player)
	elif cpu_input == "medium":
		cpu_player_medium(board, player)
	elif cpu_input == "hard":
		cpu_player_hard(board, player)


if __name__ == "__main__":
	# Enter test code below
	game_against_cpu()