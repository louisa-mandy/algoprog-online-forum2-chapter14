import pygame 
from pygame.sprite import Group 

from settings import Settings 
from game_stats import game_stats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    si_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # play button 

    play_button = Button(ai_settings, screen, "Play")

    #stats and scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #bg color 
    bg_color = (230,230,230)

    #ship, bullets, aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #fleet of aliens 
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # main loop 
    while True :
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship,
                aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship,
                aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, ship,
                aliens, bullets, play_button)
    _game()