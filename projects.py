import pygame
from sys import exit
from random import choice, randint

def collisions():
    if pygame.sprite.spritecollide(player.sprite,obstacle,  False):
        obstacle.empty()
        return False
    else:
        return True
    

class Player(pygame.sprite.Sprite):
    def __init__(self):
          super().__init__()
          player1 = pygame.image.load('images/player.png').convert_alpha()
          player2 = pygame.image.load('images/player1.png').convert_alpha()
          player3 = pygame.image.load('images/player2.png').convert_alpha()
          self.image_jump = pygame.image.load('images/player_jump.png').convert_alpha()
          self.gravity = 0
          self.player_index = 0
          self.player_list = [player1, player2, player3]
          self.image = self.player_list[self.player_index]
          self.rect = self.image.get_rect(midbottom = (80, 300))

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def player_jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom >= 300 and game_active == True:
            self.gravity = -20

    def player_animation(self):
        if self.rect.bottom < 300:
            self.image = self.image_jump
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_list): self.player_index = 0
            self.image = self.player_list[int(self.player_index)]
        
        
    def update(self):
        self.player_animation()
        self.player_jump()
        self.player_gravity()
        

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.obstacle_index = 0

        if type == "fly":
            fly_image1 = pygame.image.load('images/fly1.png').convert_alpha()
            fly_image2 = pygame.image.load('images/fly2.png').convert_alpha()
            self.list = [fly_image1, fly_image2]
            self.pos = 230
        else:
            snail_image1 = pygame.image.load('images/snail1.png').convert_alpha()
            snail_image2 = pygame.image.load('images/snail2.png').convert_alpha()
            self.list = [snail_image1, snail_image2]
            self.pos = 300

        self.image = self.list[self.obstacle_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1000), self.pos))

    def obstacle_animation(self):
        self.obstacle_index += 0.1
        if self.obstacle_index >= len(self.list):
            self.obstacle_index = 0
        self.image = self.list[int(self.obstacle_index)]

    def obstacle_reset(self):
        if game_active == False:
            self.rect.bottom == randint(900, 1100)
            start_timer = int(pygame.time.get_ticks()/ 1000)
        

    def update(self):
        self.obstacle_animation()
        self.rect.x -= 4
        self.obstacle_reset()
       

def display_score():
    current_timer = int(pygame.time.get_ticks()/800) - start_timer
    score_display = text_font.render(f'Score: {current_timer}', False, 'blue')
    score_display_rect = score_display.get_rect(center = (400, 50))
    screen.blit(score_display, score_display_rect)
    return current_timer

pygame.init()
text_font = pygame.font.Font(None, 50)
text_font1 = pygame.font.Font(None, 25)
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
game_active = False 
score = 0

#primary surfaces
sky_surface = pygame.image.load('images/new_background3.png').convert_alpha()
ground_surface = pygame.image.load('images/ground1.jpg').convert_alpha()

#message, control instruct.
game_name = text_font.render("Runner626", False, "blue")
game_name_rect = game_name.get_rect(center = (400, 50))
game_control = text_font.render("Press space to jump", False, "blue")
game_control_rect = game_control.get_rect(center = (400, 350))
game_icon = pygame.image.load('images/player_icon.png').convert_alpha()
game_icon = pygame.transform.rotozoom(game_icon, 0, 2)
game_icon_rect = game_icon.get_rect(center = (400, 200))
game_nav = text_font1.render('press p to start', False, "black")
game_nav = pygame.transform.rotozoom(game_nav, 45, 1)
game_nav_rect = game_nav.get_rect(center = (400, 380))

#objects
    #player objects
player = pygame.sprite.GroupSingle()
player.add(Player())

    #obstacle objects
obstacle = pygame.sprite.Group()

    #timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and game_active == False:
                game_active = True 
                start_timer = int(pygame.time.get_ticks()/800)


            if event.key == pygame.K_q and game_active == True:
                game_active = False
            
        if event.type == obstacle_timer:
            obstacle.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

    
    if game_active:

            #primary surface display
            screen.blit(sky_surface, (0, 0))
            screen.blit(ground_surface, (0, 300))

            #score display
            score = display_score()

            #player
            player.draw(screen)
            player.update()

            #obstacle
            obstacle.draw(screen)
            obstacle.update()

            game_active = collisions()
                    
    else:
        screen.fill((34, 145, 154))
        score_out = text_font.render(f'Your Score: {score}', False, "blue")
        score_out_rect = score_out.get_rect(center = (400, 50))
        screen.blit(game_control, game_control_rect)
        screen.blit(game_icon, game_icon_rect)
        screen.blit(game_nav, game_nav_rect)
        if score == 0:
             screen.blit(game_name, game_name_rect)
        else:
             screen.blit(score_out, score_out_rect)
    
    
    pygame.display.update()
    clock.tick(60)