# Copy and paste create_board here

# Copy and paste print_board here

# Copy and paste drop_piece here

# Copy and paste execute_player_turn here

# Copy and paste end_of_game here

# Copy and paste cpu_player_easy

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
	# Implement your solution below
	raise NotImplementedError


if __name__ == "__main__":
	# Enter test code below
	game_against_cpu()