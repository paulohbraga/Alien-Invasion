import pygame
class Settings():

	'''Classe que define os parametros do jogo Alien Invasion'''
	def __init__(self):
		'''Inicializa as configs do jogo'''
		
		# TELA
		self.game_name = 'Jogo de naves'
		self.screen_width = 500
		self.screen_height = 710
		self.bg_color = (0, 0, 0)
		# BG Espaco
		self.bg = pygame.image.load('images/space_big.png')
		self.bg2 = pygame.image.load('images/space2.png')

		self.ship_image = pygame.image.load('images/redship_no_bg.png')


		# Config NAVE
		#self.ship_speed_factor = 5
		self.ships_limit = 3
		
		# Config Alien
		self.alien_speed_factor = 2
		self.fleet_drop_speed = 10
		

		# a taxa com que a velocidade do jogo aumenta
		self.speedup_scale = 1.1
		# taxa de aumento da pontuacao
		self.score_scale = 1.5

		self.initialize_dynamic_settings()


		# Config FIRE
		self.bullet_speed_factor = 20
		self.bullet_width = 3
		self.bullets_allowed = 100
		self.bullet_height = 25
		self.bullet_color = 255,103,60
		self.bullet_sound = pygame.mixer.Sound('sounds/laser.wav')
		self.bullet_explosion = pygame.mixer.Sound('sounds/SFX_Explosion_01.wav')
		self.new_wave = pygame.mixer.Sound('sounds/phaser.wav')

		# Tiro Especial
		self.special_bullet_speed_factor = 20
		self.special_bullet_width = 2
		self.special_bullets_allowed = 5
		self.special_bullet_height = 50
		self.special_bullet_color = 255,103,60
		self.special_bullet_sound = pygame.mixer.Sound('sounds/laser.wav')
		self.special_bullet_explosion = pygame.mixer.Sound('sounds/explosion.wav')

		# Congif 
	def play_music(self):
		self.sound = pygame.mixer.music.load('sounds/space.wav')
		self.sound_playing = pygame.mixer.music.play(-1)

	def initialize_dynamic_settings(self):
		"""Inicializa as configuracoes que mudam no decorrer do jogo"""
		self.ship_speed_factor = 8
		self.bullet_speed_factor = 10
		self.alien_speed_factor = 4
		self.alien_points = 10

		# fleet_direction igual a 1 representa a direita e -1 a esqueda
		self.fleet_direction = 1

	def increase_speed(self):
		""" Aumenta as configs de velocidade"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)