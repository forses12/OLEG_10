import pygame

screen = pygame.display.set_mode([1000, 700])
import model


def view():
    screen.fill([0, 0, 0])
    model.p.sozdowatel()
    if model.event_for_debug:
        model.p.sozdowatel_debug()
    pygame.display.flip()
