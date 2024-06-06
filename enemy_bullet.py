import bullet, player

class Enemy_bullet(bullet.Bullet):
    def __init__(self,enemy,player:player.Player,bullets):
        bullet.Bullet.__init__(self,enemy,player,bullets)
        self.speed_xy=[0,5]
    def boom(self):
        if self.enemys.rect.collidepoint(self.where):
            self.h.remove(self)
            self.enemys.alive=False
            return self.where