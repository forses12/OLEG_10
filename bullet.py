
import pygame, math_utils, enemy, random,player

class Bullet():
    def __init__(self,enemy,player:player.Player):
        self.enemys=enemy
        self.player=player
        self.screen=pygame.display.get_surface()
        self.image = 'images/flies/bullet_red_down.png'
        image = pygame.image.load(self.image)
        self.image=pygame.transform.flip(image,0,1)
        self.image=pygame.transform.scale(self.image,[self.image.get_width()*4,self.image.get_height()*4])


    def sozdovatel(self):
        self.screen.blit(self.image,self.player.rect.midtop)

