import sys;
import pygame;
from pygame.sprite import Group

from settings import Settings;
from ship import Ship;
import game_functions as gf;

from pygame.sprite import Group
from game_stats import GameStats

def run_game():
	pygame.init();
	ai_settings = Settings();
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height));
	pygame.display.set_caption("Alien Invasion");
	
	stats = GameStats(ai_settings)
	
	#创建一艘飞船，一个子弹编组和一个外星人编组
	ship = Ship(ai_settings, screen);
	bullets = Group()
	aliens = Group()
	
	# 创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	
	while True:
		gf.check_event(ai_settings, screen, ship, bullets);
		
		print("stats.game_active = "+ str(stats.game_active))
		if stats.game_active:
			ship.update();
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
			
		gf.update_screen(ai_settings, screen, ship, aliens, bullets);

run_game()
