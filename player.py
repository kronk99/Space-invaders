import pygame
#import time

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, restriccion, speed):
        super().__init__()
        self.image = pygame.image.load("player_stand.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.restriccion_x = restriccion
        self.gravity = 0
        self.ready = True
        self.laser_timer = 0
        self.laser_cooldown= 600
        self.lasers= pygame.sprite.Group()

    def get_input(self):#funcion que maneja  el movimiento del jugador
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed #mueve el rectangulo en el eje x
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif pygame.KEYDOWN and keys[pygame.K_SPACE] and self.rect.bottom >=600:
            self.gravity = -15
            print(self.gravity)
        if pygame.MOUSEBUTTONUP:#DISPARA Y Pasa a "recargar"
            if pygame.mouse.get_pressed() == (True, False, False) and self.ready :
                self.shoot_laser()
                self.ready = False
                self.laser_timer = pygame.time.get_ticks()





    def update(self): #tiene que llamar todas las funciones que modifiquen al jugador
        self.falling()
        self.get_input()
        self.restriccion_eje()
        self.recharge_mouse()#llama la recarga
        self.lasers.update()

    def restriccion_eje(self):
        if self.rect.left <=0:
            self.rect.left = 0
        if self.rect.right >= self.restriccion_x:
            self.rect.right = self.restriccion_x

    def falling(self):
        self.gravity+=1
        self.rect.y +=self.gravity
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
    def recharge_mouse(self):# va analizando los tiempos de disparo con el del juego y si es mayor a 600 recarga
        if not self.ready: #pregunta si ready es false
            actual_time = pygame.time.get_ticks()
            if actual_time - self.laser_timer >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center,8,self.rect.bottom))
class Laser(pygame.sprite.Sprite):
    def __init__(self,pos, speed , abajo):
        super().__init__()
        self.image=pygame.Surface((4,20))
        self.image.fill("white")
        self.rect=self.image.get_rect(center = pos)
        self.speed = speed
        self.abajo = abajo
    def update(self):
        self.rect.y -= self.speed
        self.destroy()
    def destroy(self):
        if self.rect.y <=-10 or self.rect.y >= self.abajo:
            self.kill()








