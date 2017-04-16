from MiniBoard import MiniBoard

def Board():

	def __init__(self, size):
		self.size = size
		self.board = [[MiniBoard(size) for column in size] for row in size]

	def get_size(self):
		return self.size

	def get_board(self):
		return self.size

	def play_move(self, player, row, column, sub_row, sub_column):
		mini_board = self.get_board()[row][column]
		mini_board.play_move(player, sub_row, sub_column)
		return self.game_state()

	def game_state(self):
		return "Still on"
