import pygame


class Player:
    def __init__(self, where):
        self.image = 'images/player/player.png'
        image = pygame.image.load(self.image)
        size = [15 * 4, 16 * 4]
        self.image = pygame.transform.scale(image, size)
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(where, size)

    def sozdowatel(self):
        self.screen.blit(self.image, self.rect)

    def sozdowatel_debug(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 2)

    def control(self, event):
        for e in event:
            if e.type == pygame.MOUSEMOTION:
                self.rect.centerx = e.pos[0]
