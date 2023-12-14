import pygame

screen = pygame.display.set_mode([1000, 700])
import model


def debug(b):
    if model.event_for_debug:
        b.sozdowatel_debug()


def view():
    screen.fill([0, 0, 0])
    model.p.sozdowatel()
    model.q.sozdowatel()
    model.w.sozdowatel()
    debug(model.p)
    debug(model.q)
    debug(model.w)
    pygame.display.flip()
