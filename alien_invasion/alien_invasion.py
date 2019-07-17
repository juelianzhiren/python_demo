import sys;
import pygame;
from pygame.sprite import Group

from settings import Settings;
from ship import Ship;
import game_functions as gf;

from pygame.sprite import Group

def run_game():
	pygame.init();
	ai_settings = Settings();
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height));
	pygame.display.set_caption("Alien Invasion");
	
	#创建一艘飞创
	ship = Ship(ai_settings, screen);
	bullets = Group()
	
	bullets = Group()
	
	while True:
		gf.check_event(ai_settings, screen, ship, bullets);
		ship.update();
<<<<<<< HEAD
		bullets.update()
=======
		gf.update_bullets(bullets)
>>>>>>> b2e2948e64a06ec4e167b95da63dc5167a8e46ad
		gf.update_screen(ai_settings, screen, ship, bullets);

run_game()
