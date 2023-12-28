import pygame


class Enemy:
    def __init__(self, who, where,left,right,step_delay,step):
        self.who = who
        self.image1 = self.who
        self.image2 = self.who.replace('1', '2')
        self.where=where

        self.images = pygame.image.load(self.image1)
        self.images1 = pygame.image.load(self.image2)
        self.size = [self.images.get_width() * 4, self.images.get_height() * 4]
        self.image = pygame.transform.scale(self.images, self.size)

        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(where, self.size)

        self.p = pygame.event.custom_type()
        pygame.time.set_timer(self.p, step_delay )
        self.changed_picture = True

        self.leftx=left
        self.rightx=right
        self.speedx=step
        self.walk=True

    def a_che(self):
        if self.changed_picture:
            image = self.images1
            self.size = [self.images1.get_width() * 4, self.images1.get_height() * 4]
        else:
            image = self.images
            self.size = [self.images.get_width() * 4, self.images.get_height() * 4]
        self.changed_picture = not self.changed_picture

        center = self.rect.center
        self.rect = pygame.Rect(self.rect.topleft, self.size)
        self.rect.center = center

        self.image = pygame.transform.scale(image, self.size)

    def sozdowatel(self):
        self.screen.blit(self.image, self.rect)

    def sozdowatel_debug(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 2)
        pygame.draw.line(self.screen,[255,0,255],[self.leftx,self.rect.top],[self.leftx,self.rect.bottom],2)
        pygame.draw.line(self.screen,[255,0,255],[self.rightx,self.rect.top],[self.rightx,self.rect.bottom],2)


    def control(self, event):
        for i in event:
            if i.type == self.p and self.walk:
                self.go()

                pass
    def go(self):

            self.rect.centerx += self.speedx
            self.a_che()
            if self.rect.right >= self.rightx and self.speedx > 0:
                self.rect.right = self.rightx
                self.speedx = -self.speedx
            elif self.rect.left <= self.leftx and self.speedx < 0:
                self.rect.left = self.leftx
                self.speedx = -self.speedx
