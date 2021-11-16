import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("prueba xd")
def display_score():
    current_time=int(pygame.time.get_ticks()/1000) - start_time
    score_surface = test_font.render(f"score:{current_time}", False, "Black")
    score_rectangle= score_surface.get_rect(center = (400 , 50))
    screen.blit(score_surface, score_rectangle)

    print(current_time)
start_time = 0

clock = pygame.time.Clock()  # invoca la funcion clock

sky= pygame.image.load('sky.png').convert_alpha()
ground = pygame.image.load("ground.png").convert_alpha() # . convert_alpha=  improves rendimiento

test_font = pygame.font.Font("Pixeltype.ttf", 50)

snail_surface = pygame.image.load("snail1.png").convert_alpha()

player_surface = pygame.image.load("player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))#recordar posiciones rectangulo para la bitacora, esto crea un rectangulo alrededor de la imagen y lo mueve 300 habia abajo

snail_rectangle = snail_surface.get_rect(midbottom = (600,300))

player_gravity=0

game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE :
                game_active =True
                snail_rectangle.left = 600
                start_time = int(pygame.time.get_ticks()/1000)




    if game_active == True:
        screen.blit(sky, (0, 0))  # coloca el canvas en la pantalla,similar al .place
        screen.blit(ground, (0, 300))  # pega lo de mas abajo
        screen.blit(snail_surface,snail_rectangle)  # i could improve it by pasting it out of loop and just moving the image
        snail_rectangle.left -= 2

        display_score()
        # player:
        player_gravity += 1
        player_rectangle.y += player_gravity
        print(player_gravity)
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)
        if snail_rectangle.left == 50:
            snail_rectangle.left = 600
        if player_rectangle.colliderect(snail_rectangle):
            game_active = False
    pygame.display.update()
    clock.tick(60)