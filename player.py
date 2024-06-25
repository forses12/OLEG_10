import pygame,observer,x
CODE_DEAD=1

class Player(observer.Observer):
    def __init__(self, where,enemies):
        self.image = 'images/player/player.png'
        image = pygame.image.load(self.image)
        size = [15 * 3, 16 * 3]
        self.enemies=enemies
        self.image = pygame.transform.scale(image, size)
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(where, size)
        self.alive=True
        self.heart=3
        observer.Observer.__init__(self)
        self.j=x.X([50,50],self.heart,50,'images/player/player.png',5)
    def sozdowatel(self):
        if self.alive:
            self.screen.blit(self.image, self.rect)

        self.j.painting()
    def model(self,):
        self.hit()


    def sozdowatel_debug(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 2)

    def control(self, event):
        for e in event:
            if e.type == pygame.MOUSEMOTION:
                self.rect.centerx = e.pos[0]
    def hit(self):
        for enemy in self.enemies.copy():
            if enemy.rect.collidepoint(self.rect.center):
                self.enemies.remove(enemy)
                self.heart -= 1
                self.j.how_many = self.heart
                self._notify(CODE_DEAD)
                print(self.alive)





