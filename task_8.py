# Copy and paste create_board here

# Copy and paste print_board here

# Copy and paste drop_piece here

# Copy and paste execute_player_turn here

# Copy and paste end_of_game here

# Copy and paste local_2_player_game here

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
	

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	import os
	os.system('cls' if os.name == 'nt' else 'clear')

	
def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError