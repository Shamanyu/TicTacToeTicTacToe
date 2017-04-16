class MiniBoard():
	
	def __init__(self, size):
		self.size = size
		self.board = [[None for column in range(size)] for row in range(size)]
		self.allowed_players = ['X', 'O']
		self.game_state = None

	def get_size(self):
		return self.size

	def get_board(self):
		return self.board

	def play_move(self, player, row, column):
		if player in set(allowed_players) and row < self.get_size() and column < self.get_size() and self.get_board()[row][column] == None:
			self.board[row][column] = player
			return "Move successful"
			self.set_game_state()
		else:
			return "Invalid move"

	def get_game_state(self):
		return self.game_state

	def set_game_state(self):
		if self.get_game_state():
			pass
		else:
			player = None
			for row in self.get_size():
				for column in self.get_size():
					if not player:
						player = self.get_board()[row][column]
					elif player and self.get_board()[row][column] == player:
						continue
					else:
						player = None
						break
				if player:
					self.game_state = player
					return True
			for column in self.get_size():
				for row in self.get_size():
					if not player:
						player = self.get_board()[row][column]
					elif player and self.get_board()[row][column] == player:
						continue
					else:
						player = None
						break
				if player:
					self.game_state = player
					return True
			for index in self.get_size():
				if not player:
					player = self.get_board()[index][index]
				elif player and self.get_board()[index][index] == player:
					continue
				else:
					player = None
					break
			if player:
				self.game_state = player
				return True
			for (row, column) in zip(range(0, self.get_size()), range(self.get_size(), 0)):
				if not player:
					player = self.get_board()[row][column]
				elif player and self.get_board()[row][column] == player:
					continue
				else:
					player = None
					break
			if player:
				self.game_state = player
				return True
			return True
