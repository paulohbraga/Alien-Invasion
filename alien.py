import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''Uma classe que representa um unico alienigena'''

	def __init__(self, ai_settings, screen):
		''' Inicializa o alienigena e define a posicao inicial '''
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# Carrega a imagem do alienigena
		self.image = pygame.image.load('images/fighter.png')
		self.image2 = pygame.image.load('images/fighter.png')

		self.rect = self.image.get_rect()

		# Inicia cada novo alien proximo a parte superior esqueda da tela
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height


		# Armazena a posicao exata do alienigena
		self.x = float(self.rect.x)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True








