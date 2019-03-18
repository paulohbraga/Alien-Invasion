class GameStats():
	"""Armazena dados estatisticos do jogo """

	def __init__(self, ai_settings):
		''' Inicializa os dados'''
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		self.high_score = 0

	def reset_stats(self):
		"""Inicializa os dados que podem mudar durante o jogo"""

		self.ships_left = self.ai_settings.ships_limit
		self.fleet_drop_speed = self.ai_settings.fleet_drop_speed
		self.alien_speed_factor = self.ai_settings.alien_speed_factor
		self.score = 0
		self.level = 1



