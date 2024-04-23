import pygame, math_utils, enemy, random,player

def make_image(image):
    image1 = pygame.image.load(image)
    image = pygame.transform.scale(image1, [image1.get_width() * 3, image1.get_height() * 3])
    return image
images=[make_image('images/flies/enemy_burst1.png'),
        make_image('images/flies/enemy_burst2.png'),
        make_image('images/flies/enemy_burst3.png'),
        make_image('images/flies/enemy_burst4.png'),
        make_image('images/flies/enemy_burst5.png')]

class Kaboom():
    def __init__(self,where):
        self.p = pygame.event.custom_type()
        pygame.time.set_timer(self.p, 50)
        self.images=images.copy()
        self.where=where
    def sozdowatel(self):
        if len(self.images)!=0:
            pygame.display.get_surface().blit(self.images[0],
                                              [self.where[0]-self.images[0].get_width()/2,
                                               self.where[1]-self.images[0].get_height()/2])
    def control(self,events):
        for i in events:
            if i.type == self.p and len(self.images)!=0:
                del self.images[0]






