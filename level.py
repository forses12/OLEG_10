import math
import pygame, math_utils, enemy,random

BIG_GREEN1 = 'big_green1.png'
BUTTERFLY_RED1 = 'butterfly_red1.png'
FLY_BLUE1 = 'fly_blue1.png'


class Level:
    def __init__(self, q):
        self.screen=pygame.display.get_surface()
        self.q = q
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.sozdovatel(4, 3, 375, 625, BIG_GREEN1)
        self.sozdovatel(8, 3, 225, 775, BUTTERFLY_RED1, y=110)
        self.sozdovatel(8, 3, 225, 775, BUTTERFLY_RED1, y=160)
        self.sozdovatel(10, 3, 125, 875, FLY_BLUE1, y=210)
        self.sozdovatel(10, 3, 125, 875, FLY_BLUE1, y=260)
        self.list = [{'rects': [pygame.rect.Rect([100,100],[400,400]),
                                pygame.rect.Rect([400,200],[600,500])],
                      'enemys': [],
                      'time_sleep': 1,
                      'points': [{
                          'x': 50,
                          'y': 50,
                          'speed': 3,
                          'angle': 5
                      }
                          ,
                          {
                              'x': 150,
                              'y': 400,
                              'speed': 3,
                              'angle': 5
                          }
                          ,
                          {
                              'x': 375,
                              'y': 500,
                              'speed': 3,
                              'angle': -5
                          }
                          ,
                          {
                              'x': 480,
                              'y': 400,
                              'speed': 3,
                              'angle': -5
                          }
                          ,
                          {
                              'x': 500,
                              'y': 200,
                              'speed': 3,
                              'angle': -5
                          }
                          ,
                          {
                              'mode': 'walk',
                              'speed': 3,
                              'angle': -5

                          }
                      ]
                      }
                     ,
                     {'rects': [pygame.rect.Rect([100, 200], [200, 344]),
                                pygame.rect.Rect([300, 400], [150, 500])],
                      'enemys': [],
                      'time_sleep': 1,
                      'points': [{
                          'x': 50,
                          'y': 50,
                          'speed': 3,
                          'angle': 5
                      }
                          ,
                          {
                              'x': 150,
                              'y': 400,
                              'speed': 3,
                              'angle': 5
                          }
                          ,
                          {
                              'x': 375,
                              'y': 500,
                              'speed': 3,
                              'angle': -5
                          }
                          ,
                          {
                              'x': 480,
                              'y': 400,
                              'speed': 3,
                              'angle': -5
                          }
                          ,
                          {
                              'x': 500,
                              'y': 200,
                              'speed': 3,
                              'angle': -5
                          }
                          ,
                          {
                              'mode': 'walk',
                              'speed': 3,
                              'angle': -5

                          }
                      ]
                      }
                     ]

    def sozdovatel(self, how_many, how_many_more, left_border, right_border, p, y=60):
        f = (right_border - left_border) / how_many
        for h in range(how_many):
            l = left_border + f
            m = enemy.Enemy('images/flies/' + p, [-100, 400], how_many_more, y, left_border, l, 500, 10, 1.5)
            self.q.append(m)
            left_border = l
    def sozdowatel_debug(self):
        for f in self.list:
            for j in f['rects']:

                pygame.draw.rect(self.screen, self.color, j, 5)


