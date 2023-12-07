import pygame

class Player:
    def __init__(self,where):
        self.image='images/galaga1.png'
        self.where=where
        self.size=[15*4,16*4]
        self.screen=pygame.display.get_surface()

    def sozdowatel(self):
        image=pygame.image.load(self.image)
        image=pygame.transform.scale(image,self.size)
        self.screen.blit(image,self.where)

    def control(self,event):
        for e in event:
            if e.type==pygame.MOUSEMOTION:
                print(1)
