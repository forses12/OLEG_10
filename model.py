import pygame, player, enemy, random

import level,bullet

p = player.Player([600, 600])
q = []
k=level.Level(q)
h=[]


event_for_debug = False
normal_paint = True


def model():
    print(len(h))
    for x in h.copy():
        x.free_fly()
        if x.where[1]<0:
            h.remove(x)
