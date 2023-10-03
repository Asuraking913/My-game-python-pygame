from random import randint
import pygame 
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1500) - start_time 
    score_surface = text_font.render(f'Score: {current_time}', False, 'black')
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def player_animation():
    global player_index, player_surface
    if player_rect.bottom < 300: player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            obstacle.x -= 5

            if obstacle.bottom == 300:
                screen.blit(snail_surface, (obstacle))
            else:
                screen.blit(fly_surface, (obstacle))
    
        return obstacle_list
    
    else:
        return []

def collisions(player, obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            if player.colliderect(obstacle):
                return False
    return True

pygame.init()
screen = pygame.display.set_mode ((800, 400))
pygame.display.set_caption('ASURA KING')
text_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
game_active = False
start_time = 0 
player_gravity = 0 
player_index = 0
obstacle_rect_list = []
score = 0

#major surfaces 
sky_surfaces = pygame.image.load('images/new2.jpg').convert_alpha()
ground_surfaces = pygame.image.load('images/ground1.jpg').convert_alpha()

#player_surfaces
player1 = pygame.image.load('images/player1.png').convert_alpha()
player2 = pygame.image.load('images/player2.png').convert_alpha()
player_jump = pygame.image.load('images/player_jump.png').convert_alpha()
player_walk = [player1, player2]
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, 303))
player_icon = pygame.image.load('images/player_icon.png').convert_alpha()
player_icon = pygame.transform.rotozoom(player_icon, 0, 2)
pllayer_icon_rect = player_icon.get_rect(center = (400, 200))

#enemy 1 
snail1 = pygame.image.load('images/snail1.png').convert_alpha()
snail2 =  pygame.image.load('images/snail2.png').convert_alpha()
snail_walk = [snail1, snail2]
snail_index = 0 
snail_surface = snail_walk[snail_index]

#ememy 2 
fly1 = pygame.image.load('images/fly1.png').convert_alpha()
fly2 =  pygame.image.load('images/fly2.png').convert_alpha()
fly_walk = [fly1, fly2]
fly_index = 0
fly_surface = fly_walk[fly_index]

#timers: 1
obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer, 1500)

#timer: 2 
snail_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_timer, 500)

#timer: 3 
fly_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_timer, 100)

#into text
game_message = text_font.render('Press space bar to start and jump', False, 'black')
game_message_rect = game_message.get_rect(center = (400, 350))
game_name = text_font.render('Runner 626', False, 'black')
game_name_rect = game_name.get_rect(center = (400, 50))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 303 and game_active:
                player_gravity = -20
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                start_time = int(pygame.time.get_ticks()/ 1500)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(pygame.mouse.get_pos()):
                player_gravity = -20

        if event.type == obstacle_timer:
            if randint(0, 2):
                obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900, 1100), 230)))
        
        if event.type == snail_timer:
            if snail_index == 0: snail_index = 1
            else: snail_index = 0
            snail_surface = snail_walk[snail_index]
        
        if event.type == fly_timer:
            if fly_index == 0: fly_index = 1
            else: fly_index = 0
            fly_surface = fly_walk[fly_index]

    if game_active:
        #background setupe 
        screen.blit(sky_surfaces, (0, 0))
        screen.blit(ground_surfaces, (0, 300))
        
        
        #player_setup
        player_gravity += 1 
        player_rect.y += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 303
        player_animation()
        screen.blit(player_surface, (player_rect))

        #enemy_set up
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collisions
        game_active = collisions(player_rect, obstacle_rect_list)

        #display_score
        score = display_score()

    
    else:
        screen.fill((34, 145, 154))
        obstacle_rect_list.clear()
        player_rect.bottom = 303
        screen.blit(player_icon, (pllayer_icon_rect))
        screen.blit(game_name, (game_name_rect))
        the_score = text_font.render(f'Your score {score}', False, 'black')
        the_score_rect = the_score.get_rect(center = (400, 350))
        if score == 0:
            screen.blit(game_message, (game_message_rect))
        else:
            screen.blit(the_score, (the_score_rect))
        
    

    pygame.display.update()
    clock.tick(60)