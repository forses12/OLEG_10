
import pygame, math_utils, enemy, random,player

image = 'images/flies/bullet_red_down.png'
image1 = pygame.image.load(image)
image = pygame.transform.flip(image1, 0, 1)
image = pygame.transform.scale(image, [image.get_width() * 3, image.get_height() * 3])
class Bullet():
    def __init__(self,enemy,player:player.Player,bullets):
        self.enemys=enemy
        self.player=player
        self.screen=pygame.display.get_surface()
        self.h=bullets
        self.where=[self.player.rect.centerx-image1.get_width()/2-2,self.player.rect.centery-1]


    def sozdovatel(self):
        self.screen.blit(image,self.where)
    def free_fly(self):
        self.where[1]-=2
        self.boom()
    def boom(self):
        for k in self.enemys.copy():
            if k.rect.collidepoint(self.where):
                self.enemys.remove(k)
                self.h.remove(self)




