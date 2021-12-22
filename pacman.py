import pygame, random

pygame.init()

# variables and constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
HEADER_HEIGHT = 80

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)

BUFFER_DISTANCE = 100
PLAYER_STARTING_SCORE = 0
PLAYER_STARTING_LIVE = 5
GHOSTPCK_STARTING_VELOCITY = 5
BLUEGHOSTPACMAN_STARTING_VELOCITY = 7
YELLOWGHOSTPACMAN_STARTING_VELOCITY = 9

player_score = PLAYER_STARTING_SCORE
player_live = PLAYER_STARTING_LIVE
packman_velocity = 5
ghostpck_velocity = GHOSTPCK_STARTING_VELOCITY
blueghostpacman_velocity = BLUEGHOSTPACMAN_STARTING_VELOCITY
yellowghostpacman_velocity = YELLOWGHOSTPACMAN_STARTING_VELOCITY
acceleration = 0.5

# main surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hungry Pacman")

# images
background = pygame.image.load('SPACE.jpg')

score_backround = pygame.image.load('score_background.png').convert_alpha()
score_background_rect = score_backround.get_rect()
score_background_rect.topleft = (10,10)

live_background = pygame.image.load('score_background.png').convert_alpha()
live_background_rect = live_background.get_rect()
live_background_rect.topleft = (WINDOW_WIDTH-(live_background_rect.width+10), 10)

packman_image = pygame.image.load('PACKMAN.png').convert_alpha()
packman_image = pygame.transform.scale(packman_image, (50, 80))  #pACKMAN umenshit
packman_rect = packman_image.get_rect()
packman_rect.center = (80, WINDOW_HEIGHT//2)

ghostpck_image = pygame.image.load('ghostpck.png').convert_alpha()
ghostpck_image = pygame.transform.scale(ghostpck_image, (40, 60)) #Ghost umenshit
ghostpck_image_rect = ghostpck_image.get_rect()
ghostpck_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))

#blueghost
blueghostpacman_image = pygame.image.load('blueghostpacman.png').convert_alpha()
blueghostpacman_image = pygame.transform.scale(blueghostpacman_image, (40, 60)) #blueghost umenshit
blueghostpacman_image_rect = blueghostpacman_image.get_rect()
blueghostpacman_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))