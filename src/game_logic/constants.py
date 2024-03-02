from game_logic import display_ascii, make_image_dict
from game_logic.levels import level_one_ascii_units
import pygame

pygame.font.init()

# frames per second
FPS = 60
CLOCK = pygame.time.Clock()
START_TIME = pygame.time.get_ticks()

# FONTS
FONT_LOCATION = "/Users/Adam/Desktop/coding/games/tanks/assets/fonts/dogica.ttf"
MAIN_MUSIC_LOCATION = "/Users/Adam/Desktop/coding/games/Tanks/assets/sound/main-theme.wav"
MAIN_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/Menlo.ttc", 12)
CAPTION_FONT = pygame.font.Font(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/fonts/VictorMono-Medium.ttf", 24)
PAUSED_TEXT_COLOUR = (255, 0, 0)

# image dictionarie
TANK_IMAGES = make_image_dict.load_images_from_directory(
    "/Users/Adam/Desktop/coding/games/tanks/assets/images/units/level_one")
TERRAIN_IMAGES = make_image_dict.load_images_from_directory(
    "/Users/Adam/Desktop/coding/games/tanks/assets/images/terrain/level_one")
CAPTION_IMAGES = make_image_dict.load_images_from_directory(
    "/Users/Adam/Desktop/coding/games/tanks/assets/images/captions")
MISSILE_EXPLOSION_IMAGES = make_image_dict.load_images_from_directory(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/images/explosions/explosion_frames")
AMMO_CRATE_IMAGES = make_image_dict.load_images_from_directory(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/ammo/missile_crate")
MISSILE_IMAGES = make_image_dict.load_images_from_directory(
    "/Users/Adam/Desktop/coding/games/Tanks/assets/images/weapons/missile")

# SCREEN SETUP
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_X_MIN = 0
SCREEN_Y_MIN = 0
CENTRE_X = SCREEN_WIDTH/2
CENTRE_Y = SCREEN_HEIGHT/2
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN_BKGND = (0, 0, 0)

# ascii
CHAR_SPACING_X = -1
CHAR_SPACING_Y = 4

# PLAYER CONSTANTS
PLAYER_ACCELERATION = 6
MISSILE_ACCELERATION = 20
MISSILE_HEIGHT, MISSILE_WIDTH = MISSILE_IMAGES["player_missile"].get_height(
), MISSILE_IMAGES["player_missile"].get_width()
PLAYER_HEIGHT, PLAYER_WIDTH = display_ascii.measure_unit_size(
    level_one_ascii_units.player_tank["straight"], CHAR_SPACING_X, CHAR_SPACING_Y)
PLAYER_TANK_COLOUR = (0, 200, 255)

# enemy constants
ENEMY_TANK_COLOUR = (200, 0, 0)
ENEMY_ACCELERATION = 4
ENEMY_HEIGHT, ENEMY_WIDTH = display_ascii.measure_unit_size(
    level_one_ascii_units.enemy_tank["straight"], CHAR_SPACING_X, CHAR_SPACING_Y)
ENEMY_X_SPACING = 100

# explosions
EXPLOSION_HEIGHT, EXPLOSION_WIDTH = display_ascii.measure_unit_size(
    level_one_ascii_units.missile_explode["1"], CHAR_SPACING_X, CHAR_SPACING_Y)
