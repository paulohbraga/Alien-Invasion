from pygame.sprite import Sprite

class Ship(Sprite):
	'''Classe nave para o jogo Alien Invasion''' 

	def __init__(self, ai_settings, screen):
		''' Inicializa a nave e define sua posicao inicial'''
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		self.fire = ai_settings.bullet_sound
		self.new_wave = ai_settings.new_wave

		# Carrega a imagem da nave e obtem o rect
		self.image = ai_settings.ship_image
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Inicia cada nova nave na inferior da tela, centro
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Armazana um valor decimal para o centro da nave
		self.center = float(self.rect.centerx)

		# flag de movimento
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		''' Atualiza a posicao da nave de acordo com o flag de movimento '''

		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -=  self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.rect.bottom -=  self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom > 0:
			self.rect.top +=  self.ai_settings.ship_speed_factor



		# atualiza o objeto rect de acordo com o self.center

		self.rect.centerx = self.center

	def blitme(self):
		''' Desenha a nave em sua posicao inicial '''
		self.screen.blit(self.image, self.rect)


	def center_ship(self):
		"""Centraliza a nave na tela"""
		self.center = self.screen_rect.centerx