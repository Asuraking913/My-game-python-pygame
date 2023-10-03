import pygame
from random import choice, randint
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player1 = pygame.image.load('images/player1.png').convert_alpha()
        player2 = pygame.image.load('images/player2.png').convert_alpha()
        self.jump_image = pygame.image.load('images/player_jump.png').convert_alpha()
        self.image_states = [player1, player2]
        self.image_index = 0
        self.gravity = 0
        self.image = self.image_states[self.image_index]
        self.rect = self.image.get_rect(midbottom = (80, 303))

    def player_gravity(self):
        self.gravity += 1
        self.rect.bottom += self.gravity
        if self.rect.bottom >= 303: self.rect.bottom = 303

    def player_anime(self):
        self.image_index += 0.1
        if self.image_index >= len(self.image_states): self.image_index = 0
        self.image = self.image_states[int(self.image_index)]


    def player_jump(self):
        key = pygame.key.get_pressed()
        if self.rect.bottom < 303:
            self.image = self.jump_image
        else: 
            if key[pygame.K_UP] and self.rect.bottom == 303:
                self.gravity = -20
        
    
    def update(self):
        self.player_anime()
        self.player_gravity()
        self.player_jump()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type =='snail':
            snail_image1 = pygame.image.load('images/snail1.png').convert_alpha()
            snail_image2 = pygame.image.load('images/snail2.png').convert_alpha()
            self.obstacle_object = [snail_image1, snail_image2]
            y_pos = 303

        if type == 'fly':
            fly_image1 = pygame.image.load('images/fly1.png').convert_alpha()
            fly_image2 = pygame.image.load('images/fly2.png').convert_alpha()
            self.obstacle_object = [fly_image1, fly_image2]
            y_pos = 303
        
        self.obstacle_index = 0
        self.image = self.obstacle_object[self.obstacle_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def obstacle_movement(self):
        self.rect.x -= 3
    
    def update(self):
        self.obstacle_movement()



pygame.init()
screen = pygame.display.set_mode((800, 400))
text_font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()
game_active = False

#timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

a = pygame.image.load('images/png.png').convert_alpha()
a_rect = a.get_rect(midbottom = (80, 300))


sky_surface = pygame.image.load('images/new2.jpg').convert_alpha()
ground_surface = pygame.image.load('images/ground1.jpg').convert_alpha()

#player 
player = pygame.sprite.GroupSingle()
player.add(Player())

#obstacle
obstacle = pygame.sprite.GroupSingle()

#text
game_name =  text_font.render('Runner-modify', None, 'black')
game_name_rect = game_name.get_rect(center = (400, 50))
game_commad = text_font.render('Press up to jump', None, 'blue')
game_commad_rect = game_commad.get_rect(center = (400, 350))
game_icon = pygame.image.load('images/player_icon.png').convert_alpha()
game_icon = pygame.transform.rotozoom(game_icon, 0, 2)
game_icon_rect = game_icon.get_rect(center = (400, 200))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
            
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)

        if event.type == obstacle_timer: 
            if randint(0, 2):
                obstacle.add(Obstacle(choice(['fly', 'snail', 'snail'])))


    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(a, a_rect)

        #player
        player.draw(screen)
        player.update()

        #object
        obstacle.draw(screen)
        obstacle.update()
    
    else:
        screen.fill((34, 145, 154))
        screen.blit(game_name, game_name_rect)
        screen.blit(game_commad, game_commad_rect)
        screen.blit(game_icon, game_icon_rect)


    pygame.display.update()
    clock.tick(60)
