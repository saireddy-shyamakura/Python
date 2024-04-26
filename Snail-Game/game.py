import pygame
from sys import exit 

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock=pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
test_surface = test_font.render('My Game',False,(64,64,64))
score_surface = test_font.render('Score',False,(64,64,64))
score_rectangle = score_surface.get_rect(center = (350,100))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()   
            
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos) :
        #         print("collision")

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(300,50))
    snail_rectangle.left -= 4
    if snail_rectangle.left < 0 :
        snail_rectangle.left = 800
    screen.blit(snail_surface,snail_rectangle)
    player_rectangle.left += 1
    screen.blit(player_surface,player_rectangle)

    pygame.draw.rect(screen,'#c0e8ec',score_rectangle)
    pygame.draw.rect(screen,'#c0e8ec',score_rectangle,(6))

    screen.blit(score_surface,score_rectangle)

    # pygame.draw.line(screen,'white',(0,0),(800,400),(10))

    # if(player_rectangle.colliderect(snail_rectangle)):
    #     print("collision occured")

    # mouse_pos = pygame.mouse.get_pos()
    # if(player_rectangle.collidepoint(mouse_pos)):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)