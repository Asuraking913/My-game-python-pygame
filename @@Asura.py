from random import choice, randint
import pygame 
from sys import exit

def collisions():
    if pygame.sprite.spritecollide(player.sprite,obstacle,False):
        obstacle.empty()
        return False
    else: return True

def display_score():
    current_time = int(pygame.time.get_ticks() / 1500) - start_time
    score_message = text_font.render(f'Score: {current_time}', False, 'black')
    score_message_rect = score_message.get_rect(center = (400, 50))
    screen.blit(score_message, (score_message_rect))
    return current_time

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly1 = pygame.image.load('images/fly1.png').convert_alpha()
            fly2 = pygame.image.load('images/fly2.png').convert_alpha()
            self.obstacle_frames = [fly1, fly2]
            y_pos = 230
        else:
            snail1 = pygame.image.load('images/snail1.png').convert_alpha()
            snail2 = pygame.image.load('images/snail2.png').convert_alpha()
            self.obstacle_frames = [snail1, snail2]
            y_pos = 300
        
        self.obstacle_index = 0
        self.image = self.obstacle_frames[self.obstacle_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def obstacle_animation(self):
        self.obstacle_index += 0.1
        if self.obstacle_index > len(self.obstacle_frames): self.obstacle_index = 0
        self.image = self.obstacle_frames[int(self.obstacle_index)]


    def update(self):
        self.rect.left -= 5
        self.obstacle_animation()




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player1 = pygame.image.load('images/player1.png').convert_alpha()
        self.player2 = pygame.image.load('images/player2.png').convert_alpha()
        self.player_jump = pygame.image.load('images/player_jump.png').convert_alpha()
        self.player_index = 0
        self.gravity = 0
        self.player_frames = [self.player1, self.player2]
        self.image = self.player_frames[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 303))
    
    def apply_gravit(self):
        self.gravity += 1 
        self.rect.y += self.gravity
        if self.rect.bottom > 303: self.rect.bottom = 303


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_x] and self.rect.bottom == 303:
            self.gravity = -20

    def player_animation(self):
        if self.rect.bottom < 303: self.image = self.player_jump
        else:
            self.player_index += 0.1 
            if self.player_index > len(self.player_frames): self.player_index =  0
            self.image = self.player_frames[int(self.player_index)]

    def update(self):
        self.apply_gravit()
        self.player_input()
        self.player_animation()
        



pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Asura king')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0

#surfaces
sky_surfaces = pygame.image.load('images/new2.jpg').convert_alpha()
ground_surface = pygame.image.load('images/ground1.jpg').convert_alpha()

#player
player = pygame.sprite.GroupSingle()
player.add(Player())

#obstacle 
obstacle = pygame.sprite.Group()

#obstacle_timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1000)

#player_icon 
player_icon  = pygame.image.load('images/player_icon.png').convert_alpha()
player_icon = pygame.transform.rotozoom(player_icon, 0, 2)
player_icon_rect = player_icon.get_rect(center = (400, 200))

#icon Text
game_message1 = text_font.render('press the jump button to  jump', False, 'black')
game_message1_rect = game_message1.get_rect(center = (400, 325))
game_message = text_font.render('Press the space bar to start', False, 'black')
game_message_rect = game_message.get_rect(center = (400, 375))
game_name = text_font.render('Runner 626', False, 'black')
game_name_rect = game_name.get_rect(center = (400, 50))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/ 1500)

        if event.type == obstacle_timer:
            if randint(0, 2):
                obstacle.add(Obstacle(choice(['snail', 'fly', 'snail', 'snail'])))


    if game_active:
        screen.blit(sky_surfaces, (0, 0))
        screen.blit(ground_surface, (0, 300))

        #player
        player.draw(screen)
        player.update()

        #obstacle
        obstacle.draw(screen)
        obstacle.update()

        #display
        score = display_score()

        game_active = collisions()
       
    else:
        screen.fill((34, 134, 154))

        #offine text
        score_icon = text_font.render(f'Your score: {score}', False, 'black')
        score_icon_rect = score_icon.get_rect(center = (400, 350))
        screen.blit(player_icon, (player_icon_rect))
        screen.blit(game_name, (game_name_rect))
        
        #score display
        if score == 0:
            screen.blit(game_message1, (game_message1_rect))
            screen.blit(game_message, (game_message_rect))
        else: 
            screen.blit(score_icon, (score_icon_rect))
        


    pygame.display.update()
    clock.tick(60)


    
