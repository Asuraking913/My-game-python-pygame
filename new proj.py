import pygame
from sys import exit 





    
        

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player1 = pygame.image.load('images/player1.png').convert_alpha()
        self.player2 = pygame.image.load('images/player2.png').convert_alpha()
        self.player3 = pygame.image.load('images/player_jump.png').convert_alpha()
        self.player_index = 0
        self.player_frames = [self.player1, self.player2]
        self.gravity = 0
        self.image = self.player_frames[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 403))

    def player_gravity(self):
        self.gravity += 1 
        self.rect.y += self.gravity
        if self.rect.bottom >= 403:
            self.rect.bottom = 403
        
    def player_jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]and self.rect.bottom == 403:
            self.gravity = -20

    
    def player_anime(self):
        key = pygame.key.get_pressed()
        if self.rect.bottom < 400:
            self.image = self.player3
        else:
            self.player_index += 0.1 
            if key[pygame.K_RIGHT] or key[pygame.K_LEFT]:
                if self.player_index > len(self.player_frames): self.player_index = 0
                self.image = self.player_frames[int(self.player_index)]

    def player_walk(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]: 
            self.rect.left += 4
        elif key[pygame.K_LEFT]: 
            self.rect.left -= 4
            pass

    def screen_movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            sky_surface_rect.left -= 3
            sky_surface_rect2.left -= 3
        else:
            if key[pygame.K_LEFT]:
                sky_surface_rect.right += 3
                sky_surface_rect.right += 3
                
        
    
    def player_boundary(self):
        if self.rect.right >= 400:
            self.rect.right = 400
        elif self.rect.left <= 80:
            self.rect.left = 80

    def player_stand(self):
        if self.rect.bottom == 403:
            self.image = self.player3
        
    
   
    def object_movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            platform_rect.left -= 3
        elif key[pygame.K_LEFT] and self.rect.x > 80:
            platform_rect.right += 3
        elif key[pygame.K_LEFT] and self.rect.bottom == 403:
            platform_rect.left += 0
        elif key[pygame.K_LEFT] and self.rect.colliderect(platform0):
            self.rect.midleft = 80
            
    



    def update(self):
        self.screen_movement()
        self.player_gravity()
        self.player_jump()
        self.player_anime()
        self.player_walk()
        print(self.rect.bottom)
        self.player_boundary()
        self.object_movement()
        self.player_stand()




pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('ASURA KING')
text_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
game_active = False

sky_surface = pygame.image.load('images/new2.jpg').convert_alpha()
sky_surface = pygame.transform.rotozoom(sky_surface, 0, 2)
sky_surface2 = pygame.image.load('images/new2.jpg').convert_alpha()
sky_surface_rect = sky_surface.get_rect(topleft = (0, 0))
sky_surface_rect2 = sky_surface2.get_rect(topleft = (800, 0))
ground_surface = pygame.image.load('images/ground1.jpg').convert_alpha()

#player
player = pygame.sprite.GroupSingle()
player.add(Player())

#platform
platform0 = pygame.image.load('images/think.png').convert_alpha()
platform0_rect = platform0.get_rect(midright = (80, 403))
platform = pygame.image.load('images/grasshalfmid.png').convert_alpha()
platform_rect = platform.get_rect(midtop = (600, 250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)

    screen.blit(sky_surface, (sky_surface_rect))
    screen.blit(sky_surface2, (sky_surface_rect2))
    screen.blit(ground_surface, (0, 400))
    screen.blit(platform, (platform_rect))
    screen.blit(platform0, (platform0_rect))

    #player
    player.draw(screen)
    player.update()

    #funtions
    

    

    pygame.display.update()
    clock.tick(60)