import pygame


class Enemy:
    def __init__(self, who, where):
        self.image = who
        image = pygame.image.load(self.image)
        size = [image.get_width() * 4, image.get_height() * 4]
        self.image = pygame.transform.scale(image, size)
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(where, size)
        self.p = pygame.event.custom_type()



    def sozdowatel(self):
        self.screen.blit(self.image, self.rect)

    def sozdowatel_debug(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 2)

    def go(self,event):
        for i in event:
            if i==self.p:
                self.rect.centerx += 3
        pygame.time.set_timer(self.p, 1000)
