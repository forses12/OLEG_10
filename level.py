import math
import pygame, math_utils, enemy
BIG_GREEN1='big_green1.png'
BUTTERFLY_RED1='butterfly_red1.png'
FLY_BLUE1='fly_blue1.png'
class Level:
    def __init__(self, q):
        self.q = q
        self.sozdovatel(4, 3, 375, 625,BIG_GREEN1)
        self.sozdovatel(8, 3, 225, 775,BUTTERFLY_RED1, y=110)
        self.sozdovatel(8, 3, 225, 775,BUTTERFLY_RED1, y=160)
        self.sozdovatel(10, 3, 125, 875,FLY_BLUE1, y=210)
        self.sozdovatel(10, 3, 125, 875,FLY_BLUE1, y=260)

    def sozdovatel(self, how_many, how_many_more, left_border, right_border,p, y=60):
        f = (right_border - left_border) / how_many
        for h in range(how_many):
            l = left_border + f
            m = enemy.Enemy('images/flies/'+p, [-100, 400], how_many_more, y, left_border, l, 500, 10, 1.5)
            self.q.append(m)
            left_border = l
