# Copy and paste validate_input here

# Copy and paste create_board here

# Copy and paste print_board here

# Copy and paste drop_piece here

# Copy and paste execute_player_turn here

# Copy and paste end_of_game here

#Don't forget to include any helper functions you may have created


def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	import os
	os.system('cls' if os.name == 'nt' else 'clear')
	

def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	# Implement your solution below
	raise NotImplementedError


if __name__ == "__main__":
	# Enter test code below
	local_2_player_game()