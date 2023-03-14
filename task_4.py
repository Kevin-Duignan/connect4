# Kevin
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
	# Implement your solution below


def create_board():
	# Copy your solution from task 2 here
	raise NotImplementedError


if __name__ == "__main__":
	# Enter test code below
	board = create_board()
	drop_piece(board, 1, 3)
	for row in board:
		print(row)