import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
import space as space
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from Background import Background

def run_game():

	# Inicializa o jogo e cria um objeto na tela
	pygame.init()
	pygame.mixer.init()

	# Inicializa uma instancia de Settings():
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.game_name)
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	stats = GameStats(ai_settings)

	sb = Scoreboard(ai_settings, screen, stats)
	bg = Background(screen)

	sound_playing = ai_settings.play_music()
	alien = Alien(ai_settings, screen)
	# Cria botao play
	play_button = Button(ai_settings, screen, 'Play')

	# Cria um frota de alienigenas


	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Inicia o laco principal do jogo


	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)


		# importa as funcoes do modulo game_functions
		#space_scrolling
		if stats.game_active:
			sound_playing
			ship.update()
			bullets.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
			bg.update()
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button,bg)


run_game()
