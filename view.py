import pygame

screen = pygame.display.set_mode([1000, 700])
import model


def view():
    screen.fill([0, 0, 0])
    model.p.sozdowatel()
    pygame.display.flip()
