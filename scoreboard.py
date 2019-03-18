import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	""" Uma classe para mostrar informacaoes sobre pontuacao """

	def __init__(self, ai_settings, screen, stats):
		""" Inicializa os atributos de pontuacao"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		# Config de fonte para a pontuacao
		self.text_color = (255, 192, 192)
		self.font = pygame.font.SysFont(None, 25)

		# Prepara a imagem para pontuacao inicia
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		""" transforma a pontuacao em imagem render """
		rounded_score = int(round(self.stats.score, -1))
		score_str = "SCORE: {:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 10

	def prep_high_score(self):
		""" Transforma a pontuacao maxina em uma imagem renderizada """
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "HIGH SCORE: {:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

		# Centraliza a pontuacao maxina na parte superior da tela 
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		""" Transforma o nivel e uma imagem renderizada """
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

		# Posiciona o nivel abaixo da pontuacao
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top =  self.score_rect.bottom + 10

	def prep_ships(self):
		""" Mostra quantas naves restam """
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 5 + ship_number * ship.rect.width
			ship.rect.y = 5
			self.ships.add(ship)

	def show_score(self):
		""" Desenha a pontuacao na tela """
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)

		# desenha as naves restantes
		self.ships.draw(self.screen)