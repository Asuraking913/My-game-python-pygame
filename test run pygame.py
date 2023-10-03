import pygame 




pygame.init()
screen = pygame.display.set_mode ((800, 600))
pygame.display.set_caption('ASURA KING')
text_font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
active = True 


surface = pygame.image.load('images/bomb.png').convert_alpha()
surface_rect = surface.get_rect(midbottom = (80, 300))

load = text_font.render('Loading....', False,(23, 134 ,145))
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
        surface_rect.x += 3
    else:
        surface_rect.x -= 0

    
    if surface_rect.x >= 100:
        surface_rect.y -= 3
        active = False
    
    if surface_rect.y <= 300:
        surface_rect.x -= 3

    if surface_rect.x <= 80:
        surface_rect.y += 3
    
    if surface_rect.y >= 350:
        surface_rect.x += 3
    
    
    screen.blit(surface, (surface_rect))
    screen.blit(load, (load_rect))


    pygame.display.update()
    clock.tick(60)