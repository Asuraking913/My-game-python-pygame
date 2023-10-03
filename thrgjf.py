import pygame
from sys import exit

#global variables
sky_x = 0
sky_y = 0 


class platfor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        platform1 = pygame.image.load('images/grass.jpg').convert_alpha()
        platform2 = pygame.images .load('images/grass2.png').convert_alpha()
        
        pass

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image1 = pygame.image.load('images/player1.png').convert_alpha()
        image2 = pygame.image.load('images/player2.png').convert_alpha()
        self.images_jump = pygame.image.load('images/player_jump.png').convert_alpha()
        self.image_states = [image1, image2]
        self.image_index = 0
        self.gravity = 0
        self.key = pygame.key.get_pressed()
    
        self.image = self.image_states[self.image_index]
        self.rect = self.image.get_rect(midbottom = (80, 200))

    def player_anime(self):
        key = pygame.key.get_pressed()
        self.image_index += 0.1
        if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
            if self.image_index >= len(self.image_states): self.image_index = 0
            self.image = self.image_states[int(self.image_index)]
        
        #screen movement in player amimation method
        if self.key[pygame.K_RIGHT] and self.rect.x == 400:
            sky_surface_rect.x += 1
        else: 
            if self.key[pygame.K_LEFT] and self.rect.x == 200:
                sky_surface_rect.x -= 1

    def player_movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]  and self.rect.x < 500:
            self.rect.x += 2.5
        elif key[pygame.K_LEFT] and self.rect.x >= 80:
            self.rect.x -= 2.5


    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity 
        if self.rect.bottom >= 303:
            self.rect.bottom = 303

    def player_jump(self):
        key = pygame .key.get_pressed()
        if key[pygame.K_UP] and self.rect.bottom == 303:
            self.gravity = -20
        elif key[pygame.K_UP] and self.rect.bottom < 303:
            self.image = self.images_jump
        else:
            if self.rect.bottom == 303:
                self.image = self.image_states[0]


        #screen method
    def scr_move_player(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and self.rect.x == 500:
            sky_surface_rect.x += 1.5

    def scr_movement_player(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            sky_surface_rect += 1 

    
        #trying to return the value of self.rect at this point to use an if or else statement to determine the outcome of the background using its index

    def update(self):
        self.player_jump()
        self.player_movement()
        self.player_gravity()
        self.player_anime()
        self
        

        #scr method calling
        self.scr_move_player()
        
        

pygame.init()
screen = pygame.display.set_mode((800, 400))
text_font = pygame.font.Font(None, 50)
title = pygame.display.set_caption('Little Tang')
time = pygame.time.Clock()
game_active = False 

#player
player = pygame.sprite.GroupSingle()
player.add(Player())

#screen_surfaces
background_lists = []
surface1 = pygame.image.load('images/new_background1.png').convert_alpha()
surface2 = pygame.image.load('images/new_background2.png').convert_alpha()
surface3 = pygame.image.load('images/new_background3.png').convert_alpha()
surface4 = pygame.image.load('images/new_background4.png').convert_alpha()
surface_index = 0
surface_lists = [surface1, surface2, surface3, surface4]
surface = surface_lists[surface_index]
sky_surface_rect = surface.get_rect(topleft = (0, 0))
ground_surface = pygame.image.load('images/ground1.jpg').convert_alpha()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = True

        if event.type == pygame.MOUSEMOTION:
            print(event.pos)

    if game_active:

        #screen display
        screen.blit(surface, (sky_surface_rect))
        screen.blit(ground_surface, (0, 300))

        #player
        player.draw(screen)
        player.update()
        



        
    else:
        screen.fill((54, 134, 154))

    pygame.display.update()
    time.tick(60)






#next phase is to create the background lists so that the game can select from a group of backgrounds to display as an intro into another world then we would decide if to move to the platform or probably choose the obstacles of the game