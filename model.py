import pygame, player, enemy, random

import level,bullet

p = player.Player([600, 600])
q = []
k=level.Level(q)
h=bullet.Bullet(q, p)


event_for_debug = False
normal_paint = True


def model():
    pass
