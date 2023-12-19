import pygame


class Enemy:
    def __init__(self, who, where):
        self.who = who
        self.image1 = self.who
        self.image2 = self.who.replace('1','2')


        self.images = pygame.image.load(self.image1)
        self.images1 = pygame.image.load(self.image2)
        self.size = [self.images.get_width() * 4, self.images.get_height() * 4]
        self.image = pygame.transform.scale(self.images, self.size)

        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(where, self.size)

        self.p = pygame.event.custom_type()
        pygame.time.set_timer(self.p, 500)
        self.b=True

    def a_che(self):
        if self.b:
            image=self.images1

        else:
            image=self.images

        self.b= not self.b
        self.image = pygame.transform.scale(image, self.size)
    def sozdowatel(self):
        self.screen.blit(self.image, self.rect)

    def sozdowatel_debug(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 2)

    def go(self,event):
        for i in event:
            if i.type==self.p:
                self.rect.centerx += 6
                self.a_che()






