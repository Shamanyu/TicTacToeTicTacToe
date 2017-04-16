from MiniBoard import MiniBoard

def Board():

	def __init__(self, size):
		self.size = size
		self.board = [[MiniBoard(size) for column in size] for row in size]
		self.game_state = None
		self.allowed_players = ['X', 'O']

	def get_size(self):
		return self.size

	def get_board(self):
		return self.size

	def play_move(self, player, row, column, sub_row, sub_column):
		mini_board = self.get_board()[row][column]
		mini_board.play_move(player, sub_row, sub_column)
		return self.game_state()

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
						player = self.get_board()[row][column].get_game_state()
					elif player and self.get_board()[row][column].get_game_state() == player:
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
						player = self.get_board()[row][column].get_game_state()
					elif player and self.get_board()[row][column].get_game_state() == player:
						continue
					else:
						player = None
						break
				if player:
					self.game_state = player
					return True
			for index in self.get_size():
				if not player:
					player = self.get_board()[index][index].get_game_state()
				elif player and self.get_board()[index][index].get_game_state() == player:
					continue
				else:
					player = None
					break
			if player:
				self.game_state = player
				return True
			for (row, column) in zip(range(0, self.get_size()), range(self.get_size(), 0)):
				if not player:
					player = self.get_board()[row][column].get_game_state()
				elif player and self.get_board()[row][column].get_game_state() == player:
					continue
				else:
					player = None
					break
			if player:
				self.game_state = player
				return True
			return True

