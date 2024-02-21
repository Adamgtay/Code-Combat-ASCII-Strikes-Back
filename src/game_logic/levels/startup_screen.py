import pygame
from game_logic import constants, event_handler, blit_text


def startup_screen(game_running):
    # game loop
    while game_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - constants.START_TIME

        blit_text.display_text(constants.SCREEN,"startup screen",constants.MAIN_FONT,constants.SCREEN_WIDTH/2,constants.SCREEN_HEIGHT/2,(255,0,0))


        game_running = event_handler.event_handler_startup(game_running)


        pygame.display.update() 
        constants.CLOCK.tick(constants.FPS)