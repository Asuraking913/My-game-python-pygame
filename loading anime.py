import pygame 




pygame.init()
screen = pygame.display.set_mode ((800, 600))
pygame.display.set_caption('ASURA KING')
text_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
active = True 


surface = pygame.image.load('images/bomb.png').convert_alpha()
surface_rect = surface.get_rect(midbottom = (80, 300))

load_index = 0
load1 = text_font.render('Loading.', False,('black'))
load2 = text_font.render('Loading..', False,('black'))
load3 = text_font.render('Loading...', False,('black'))
load4 = text_font.render('Loading....', False,('black'))
load_list = [load1, load2, load3, load4]
load  = load_list[0]
load_rect = load.get_rect(midbottom  = (135, 469))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)

    
    screen.fill((45, 134, 56))

    if active:
        surface_rect.x += 2
    else:
        surface_rect.x -= 0

    
    if surface_rect.x >= 100:
        surface_rect.y -= 2 
        active = False
    
    if surface_rect.y <= 300:
        surface_rect.x -= 2

    if surface_rect.x <= 80:
        surface_rect.y += 2
    
    if surface_rect.y >= 350:
        surface_rect.x += 2
    
    
    screen.blit(surface, (surface_rect))

    load_index += 0.1
    if load_index >= len(load_list): load_index = 0
    load = load_list[int(load_index)]
    screen.blit(load, (load_rect))


    pygame.display.update()
    clock.tick(120)