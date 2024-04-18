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
p = pygame.event.custom_type()
pygame.time.set_timer(p,1000)
class Kaboom():
    def __init__(self,    ):
        self.images=images
    def sozdowatel(self):
        pygame.display.get_surface().blit(self.images[0], [500, 500])
    def control(self,events):
        for i in events:
            if i.type == p and len(self.images)!=0:
                del self.images[0]






