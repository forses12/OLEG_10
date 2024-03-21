import pygame, player, enemy, random

import level

p = player.Player([600, 600])
q = []
k=level.Level(q)

# def sozdovatel(how_many):
#     p = 100
#     for h in range(how_many):
#
#         # y = random.randint(-100, 400)
#         # if y < 0:
#         #     x = random.randint(-100, 1100)
#         # else:
#         #     n = [random.randint(-100, 0), random.randint(1000, 1100)]
#         #     x = random.choice(n)
#         l = p + 800 / how_many
#         m = enemy.Enemy('images/flies/butterfly_red1.png', [-100,400], 100, p, l, 500, 30, 1.5)
#         p = l
#         q.append(m)
#
# sozdovatel(4)
# q[0].walk = False


event_for_debug = False
normal_paint = True


def model():
    pass
