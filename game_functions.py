import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		# Move a nave pra direita
		ship.moving_right = True

	elif event.key == pygame.K_LEFT:
		# Move a nave pra direita
		ship.moving_left = True
	
	# elif event.key == pygame.K_UP:
	# 	# Move a nave pra direita
	# 	ship.moving_up = True

	# elif event.key == pygame.K_DOWN:
	# 	# Move a nave pra direita
	# 	ship.moving_down = True

	elif event.key == pygame.K_q:
		sys.exit()

	# Checa espaco para disparar projetil
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		ship.fire.play()
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def check_keyup_events(event, ship):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = False

	elif event.key == pygame.K_LEFT:
		# Move a nave pra direita
		ship.moving_left = False

	elif event.key == pygame.K_UP:
		# Move a nave pra cima
		ship.moving_up = False

	elif event.key == pygame.K_DOWN:
		# Move a nave pra baixo
		ship.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
	# Observa os eventos do teclado e mouse
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	"""Inicia um novo jogo quando clicar em play"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		ai_settings.initialize_dynamic_settings()
		# reinicia os dados estatisticos do jogo
		stats.reset_stats()
		stats.game_active = True

		# reinicia as imagens de pontuacao ao clicar play()
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()


		# esconde o ponteiro do mouse
		pygame.mouse.set_visible(False)
		aliens.empty()
		bullets.empty()

		# cria uma nova frota e centraliza a nava
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, bg):
	# Redesenha a tela a cada pessagem pelo laco

	screen.fill(ai_settings.bg_color) # Define a cor de fundo
	bg.render()
	# Define o background de acordo com o nivel(par ou impar)
	#if stats.level % 2 != 0:
	#	screen.blit(ai_settings.bg,(0,0))
	#else:
#		screen.blit(ai_settings.bg2,(0,0))
	# Redesenha o projetil atras da nave e dos alienigenas
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	# Desenha a nave definida na classe Ship()
	sb.show_score()
	ship.blitme()
	aliens.draw(screen)

	# Desenha o botao play
	if not stats.game_active:
		play_button.draw_button()


	# Deixa a tela mais recent visivel
	pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
			# print(len(bullets))
	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):

	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	if collisions:
		ai_settings.bullet_explosion.play()
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)
	
	if len(aliens) == 0:
		# Destroi os projeteis existentes e repovoa  a frota de aliens	
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, ship, aliens)

		# aumenta o nivel
		stats.level += 1
		sb.prep_level()

def get_number_aliens_x(ai_settings, alien_width):
	''' Determina o numero de aliens  que cabem numa linha'''
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	""" Determina o numero de linhas com aliens cabem na tela """
	available_space_y = (ai_settings.screen_height - (3 * alien_height) - alien_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	# Cria um alien e posiciona a linha
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	
	aliens.add(alien)

def create_fleet(ai_settings, screen, ship,  aliens):
	"""Cria uma frota de alienigenas"""
	# Cria a alien e calcula o numero de alien em uma linha
	# O espaco entre os aliens e igual a altura de um alienigena

	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)


	# Cria a frota de aliens 
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
	'''Atualiza as posicoes de todos os aliens da frota'''
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
	check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
	""" Responde ao fato de nave ter sido atingida por um alien """
	if stats.ships_left > 0:
		# Decrementa ships_left
		stats.ships_left -= 1

		# atualiza o painel de naves restantes
		sb.prep_ships()

		# Esvazia a lista de aliens e projeteis
		aliens.empty()
		bullets.empty()

		# Cria uma nova frota e centraliza a nave
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		#Faz uma pausa
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""Verifica se algum alien atingiu a parte inferior da tela"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Trata esse caso do mesmo modo que e feito quando a nave e atingida
			ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
			break


def  check_high_score(stats, sb):
	""" Verifica se ha uma nova pontuacao maxima """
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()










