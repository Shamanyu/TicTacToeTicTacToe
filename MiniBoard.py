class MiniBoard():
	
	def __init__(self, size):
		self.size = size
		self.board = [[None for column in range(size)] for row in range(size)]
		self.allowed_players = ['X', 'O']

	def get_size(self):
		return self.size

	def get_board(self):
		return self.board

	def play_move(self, player, row, column):
		if player in set(allowed_players) and row < self.get_size() and column < self.get_size() and self.get_board()[row][column] == None:
			self.board[row][column] = player
			return self.game_state()

	def game_state(self):
		return "Still on"
