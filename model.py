import pygame, player, enemy, random

import level,bullet,kaboom,kaboom_player
def it_rip():
    s.append(kaboom_player.Kaboom_player(p))



q = []
h=[]
s=[]
p = player.Player([600, 600],q,it_rip)
k=level.Level(q,p,h)
event_for_debug = False
normal_paint = True


def model():

    for x in h.copy():
        b=x.free_fly()
        if x.where[1]<0:
            h.remove(x)
        if b is not None:
            if type(x) is bullet.Bullet:
                j = kaboom.Kaboom(b)
            else:
                j = kaboom_player.Kaboom_player(p)
            s.append(j)



