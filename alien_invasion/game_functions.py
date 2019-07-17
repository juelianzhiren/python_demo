import sys;
import pygame;

from bullet import Bullet

def check_keydown_event(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True;
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True;
<<<<<<< HEAD
	elif event.type == pygame.K_SPACE:
		new_bullets = Bullet(ai_settings, screen, ship)
=======
	elif event.key == pygame.K_SPACE:
		fire_bulles(ai_settings, screen, ship, bullets)

def fire_bulles(ai_settings, screen, ship, bullets):
	"""如果还没有达到限制，就发射一颗子弹"""
	#创建一颗子弹，并将其加入到编组bullets中
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
>>>>>>> b2e2948e64a06ec4e167b95da63dc5167a8e46ad
		bullets.add(new_bullet)
		
def check_keyup_event(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False;
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False;		

def check_event(ai_settings, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit();
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event, ai_settings, screen, ship, bullets);
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, ship);
		

def update_screen(ai_settings, screen, ship, bullets):
	"""更新屏幕上的图像，并切换到新屏幕上"""
	#每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color);
<<<<<<< HEAD
	
	for bullet in bullets.sprites():
		bullet.draw_bullet();
	
=======
	for bullet in bullets.sprites():
		bullet.draw_bullet()
>>>>>>> b2e2948e64a06ec4e167b95da63dc5167a8e46ad
	ship.blitme();
	
	#让最近绘制的屏幕课件
	pygame.display.flip();

def update_bullets(bullets):
	"""更新子弹的位置，并删除已消失的子弹"""
	#更新子弹的位置
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))