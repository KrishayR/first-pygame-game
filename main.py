import pygame,sys
from pygame.locals import *
import time
pygame.init()

screen = pygame.display.set_mode((800,600),pygame.RESIZABLE)
clock = pygame.time.Clock()
def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,500))
    screen.blit(floor_surface,(floor_x_pos + 650,500))
def player1_animation():
    new_player = anim_frames[anim_index]
    new_player_rect = new_player.get_rect(center = (150,player1_rect.centery))
    return new_player,new_player_rect
def create_car():
    new_car = car_surface.get_rect(midbottom = (900,515))
    return new_car
def move_car(cars):
    for car in cars:
        car.centerx -= 65
    return cars
def draw_car(cars):
    for car in cars:
        screen.blit(car_surface,car)
def check_collision(cars):
    for car in cars:
        if player1_rect.colliderect(car):
                screen.blit(injury_screen,injury_rect)
                time.sleep(5)
                screen.blit(bg_surface,(rel_x - bg_surface.get_rect().width ,0))
                return True
    return False
 

bg_surface = pygame.image.load('documents/game/bgamenight.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (800,600))
car_surface = pygame.image.load('documents/game/car.png').convert_alpha()
car_surface = pygame.transform.scale(car_surface, (150,75))
car_list = []
SPAWNCAR = pygame.USEREVENT
pygame.time.set_timer(SPAWNCAR,8000)
floor_surface = pygame.image.load('documents/game/floor.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (800,200))
floor_x_pos = 0
x = 0 
isjump = True
jumpcount = 12
injury = False
anim1 = pygame.image.load('documents/game/astro.png').convert_alpha()
anim1 = pygame.transform.scale(anim1, (300,200))
anim2 = pygame.image.load('documents/game/astro2.png').convert_alpha()
anim2 = pygame.transform.scale(anim2, (300,200))
anim3 = pygame.image.load('documents/game/astro3.png').convert_alpha()
anim3 = pygame.transform.scale(anim3, (300,200))
anim5 = pygame.image.load('documents/game/astro5.png').convert_alpha()
anim5 = pygame.transform.scale(anim5, (300,200))
anim4 = pygame.image.load('documents/game/astro4.png').convert_alpha()
anim4 = pygame.transform.scale(anim4, (300,200))
anim_frames = [anim1,anim2,anim3,anim5,anim4]
anim_index = 0
player1 = anim_frames[anim_index]
player1_rect = player1.get_rect(center = (300,475))
injury_screen = pygame.image.load('documents/game/injuryscreen.png').convert_alpha()
injury_screen = pygame.transform.scale(injury_screen,(800,600))
injury_rect = injury_screen.get_rect(center = (400,300))
ANIMRUN = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMRUN,50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()         
        if event.type == ANIMRUN:
            if anim_index < 3:
                anim_index += 1
            else:
                anim_index = 0
            player1,player1_rect = player1_animation()
        if event.type == SPAWNCAR:
            car_list.append(create_car())
        if not(isjump):  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    isjump = True
                if event.key == pygame.K_UP:
                    isjump = True
        else:
            if jumpcount >= -12:
                neg = 1
                if jumpcount < 0:
                    neg = -1
                player1_rect.centery -= (jumpcount ** 2) * 1 * neg
                jumpcount -= 2
            else:
                isjump = False
                jumpcount = 12
        if injury == True:
            screen.blit(injury_screen,injury_rect)

        
    rel_x = x % bg_surface.get_rect().width
    screen.blit(bg_surface,(rel_x - bg_surface.get_rect().width ,0))
    if rel_x <= 800:
        screen.blit(bg_surface,(rel_x,0))
    x -= 10
    floor_x_pos -= 30
    draw_floor()
    if floor_x_pos <= -100:
        floor_x_pos = 0
    car_list = move_car(car_list)
    draw_car(car_list)
    injury = check_collision(car_list)
    screen.blit(player1,player1_rect) 
    screen.blit(floor_surface,(floor_x_pos,500))
    pygame.display.update()
    clock.tick(15)
