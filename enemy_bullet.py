import bullet, player ,pygame
image = 'images/flies/bullet_blue_down.png'
image = pygame.image.load(image)
image = pygame.transform.scale(image, [image.get_width() * 3, image.get_height() * 3])
class Enemy_bullet(bullet.Bullet):
    def __init__(self,enemy,player:player.Player,bullets):
        bullet.Bullet.__init__(self,enemy,player,bullets)
        self.speed_xy=[0,5]
        self.image=image
    def boom(self):
        if self.enemys.rect.collidepoint(self.where):
            self.h.remove(self)
            self.enemys.alive=False
            return self.where