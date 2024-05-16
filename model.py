import pygame, player, enemy, random

import level,bullet,kaboom

q = []
p = player.Player([600, 600],q)
k=level.Level(q)
h=[]
s=[]
event_for_debug = False
normal_paint = True


def model():

    for x in h.copy():
        b=x.free_fly()
        if x.where[1]<0:
            h.remove(x)
        if b is not None:
            j = kaboom.Kaboom(b)
            s.append(j)


