# Kevin
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

def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	random_column = random.randint(1, 7)
	while True:
		if drop_piece(board, player, random_column):
			return random_column

print(cpu_player_easy([
[1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 1, 1, 1]
], 2))