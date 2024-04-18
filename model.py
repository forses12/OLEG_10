import pygame, player, enemy, random

import level,bullet,kaboom

p = player.Player([600, 600])
q = []
k=level.Level(q)
h=[]
s=kaboom.Kaboom()


event_for_debug = False
normal_paint = True


def model():
    print(len(h))
    for x in h.copy():
        x.free_fly()
        if x.where[1]<0:
            h.remove(x)
