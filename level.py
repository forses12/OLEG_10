import math
import pygame, math_utils,enemy

class Level:
    def __init__(self,q):
        self.q=q
        self.sozdovatel(4,350,650)
        self.sozdovatel(8,200,800,y=160)
    def sozdovatel(self,how_many,left_border,right_border,y=100):
        f=(right_border-left_border)/how_many
        for h in range(how_many):
            l=left_border+f
            m = enemy.Enemy('images/flies/butterfly_red1.png', [-100,400], y, left_border, l, 500, 10, 1.5)
            self.q.append(m)
            left_border=l

