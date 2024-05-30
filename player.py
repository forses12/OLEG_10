import pygame


class Player:
    def __init__(self, where,enemies, kaboom_callback):
        self.image = 'images/player/player.png'
        image = pygame.image.load(self.image)
        size = [15 * 3, 16 * 3]
        self.kaboom_callback=kaboom_callback
        self.enemies=enemies
        self.image = pygame.transform.scale(image, size)
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(where, size)
        self.alive=True

    def sozdowatel(self):
        self.hit()
        if self.alive:
         self.screen.blit(self.image, self.rect)

    def sozdowatel_debug(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 2)

    def control(self, event):
        for e in event:
            if e.type == pygame.MOUSEMOTION:
                self.rect.centerx = e.pos[0]
    def hit(self):
        for enemy in self.enemies:
            if enemy.rect.collidepoint(self.rect.center):
                self.alive=False
                self.kaboom_callback()





