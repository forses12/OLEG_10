import pygame

screen = pygame.display.set_mode([1000, 700])
import model


def debug(b):
    if model.event_for_debug:
        b.sozdowatel_debug()


def view():
    screen.fill([0, 0, 0])
    if model.normal_paint:
        model.p.sozdowatel()
        for a in model.q:
            a.sozdowatel()


    debug(model.p)
    for a in model.q:
        debug(a)
    debug(model.k)


    pygame.display.flip()
