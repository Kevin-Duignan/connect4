# Copy and paste validate_input here
# Copy and paste create_board here
# Copy and paste drop_piece here

def execute_player_turn(player, board): # Task 5
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	raise NotImplementedError


if __name__ == "__main__":
	# Enter test code below
	board = create_board()
	move = execute_player_turn(1, board)
	print(move)