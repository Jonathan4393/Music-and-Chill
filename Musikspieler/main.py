import pygame,sys
from os import walk

pygame.init()
screen = pygame.display.set_mode((500,300))
pygame.display.set_caption('Music and Chill')

standard_path = 'music\\'
music_loading = None
music_playing = None
run = True

music_names = list(walk('music\\'))[0]


def handle_buttons():
	time = pygame.mixer.music.get_pos()
	pos = pygame.mouse.get_pos()

	if play_button_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
		music_loading = music_names[-1][0]
		music_playing = pygame.mixer.music.load(f'{standard_path}{music_loading}')
		pygame.mixer.music.play()

	# if forward_button_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
	# 	if pygame.mixer.music.get_busy():
	# 		pygame.mixer.music.rewind()
	# 		new_time = time + 10000  # Füge 10 Sekunden (10000 Millisekunden) hinzu
	# 		pygame.mixer.music.set_pos(new_time)




play_button_surf_pro = pygame.image.load('data/play.png').convert_alpha()
play_button_surf = pygame.transform.scale(play_button_surf_pro,(80,80))
play_button_rect = play_button_surf.get_rect(center = (250,150))

forward_button_surf = pygame.image.load('data/forward.png')
forward_button_rect =  forward_button_surf.get_rect(center = (330,150))

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()



	# updating

	handle_buttons()


	def draw():
		screen.fill((237,231,156))
		screen.blit(play_button_surf,(play_button_rect))
		# screen.blit(forward_button_surf,(forward_button_rect))

	draw()

	pygame.display.update()