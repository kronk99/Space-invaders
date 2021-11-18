import sys
from player import Player

import pygame
#from sys import exit
pygame.init()
#main display :
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space invaders")
clock = pygame.time.Clock() #summons the clock function
FLAG = True
class Game:
    def __init__(self):
        player = Player((400, 620), 800 , 5)
        self.player=pygame.sprite.GroupSingle(player)
    def run(self):
        self.player.update()#Updates the sprite rectangle to move
        self.player.draw(screen)
        self.player.sprite.lasers.draw(screen)
def main():
    game=Game()
    Flag = True
    while Flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Flag=False
        screen.fill((30,30,30))
        game.run()  # llama la funcion run de game
        pygame.display.flip()#debe ir debajo de todo lo que le agrego, "voltea" lo que este debajo del fill
        clock.tick(60)
    pygame.quit()
    sys.exit()
main()


