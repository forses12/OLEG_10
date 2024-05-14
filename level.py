import math
import pygame, math_utils, enemy, random

BIG_GREEN1 = 'big_green1.png'
BUTTERFLY_RED1 = 'butterfly_red1.png'
FLY_BLUE1 = 'fly_blue1.png'


class Level:
    def __init__(self, q):
        self.screen = pygame.display.get_surface()
        self.q = q
        self.sozdovatel(4, 3, 375, 625, BIG_GREEN1)
        self.sozdovatel(8, 3, 225, 775, BUTTERFLY_RED1, y=110)
        self.sozdovatel(8, 3, 225, 775, BUTTERFLY_RED1, y=160)
        self.sozdovatel(10, 3, 125, 875, FLY_BLUE1, y=210)
        self.sozdovatel(10, 3, 125, 875, FLY_BLUE1, y=260)
        self.list = [{'rects': [pygame.rect.Rect([440, 100], [110, 70]),
                                ],
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
                     {'rects': [pygame.rect.Rect([422, 200], [140, 70])],

                      'enemys': [],
                      'time_sleep': 2,
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
                     {'rects': [pygame.rect.Rect([360,30], [250, 60]),
                                pygame.rect.Rect([360,100], [60, 70]),
                                pygame.rect.Rect([560,100], [60, 70])],

                      'enemys': [],
                      'time_sleep': 3,
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
                     {'rects': [pygame.rect.Rect([220, 100], [120, 70]),
                                pygame.rect.Rect([625, 100], [120, 70])],

                      'enemys': [],
                      'time_sleep': 4,
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
                     {'rects': [pygame.rect.Rect([270, 200], [120, 70]),
                                pygame.rect.Rect([570, 200], [120, 70])],

                      'enemys': [],
                      'time_sleep': 6,
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
                     {'rects': [pygame.rect.Rect([120, 200], [120, 70]),
                                pygame.rect.Rect([720, 200], [120, 70])],

                      'enemys': [],
                      'time_sleep':9 ,
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
        self.zapusk()
        self.rects_team()

    def sozdovatel(self, how_many, how_many_more, left_border, right_border, p, y=60):
        f = (right_border - left_border) / how_many

        for h in range(how_many):
            l = left_border + f
            m = enemy.Enemy('images/flies/' + p, [-100, 400], how_many_more, y, left_border, l, 500, 10, 1.5)
            self.q.append(m)
            left_border = l

    def sozdowatel_debug(self):

        for f in self.list:
            if 'color' not in f:
                f['color']=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            for j in f['rects']:
                pygame.draw.rect(self.screen, f['color'], j, 5)
    def rects_team(self):
        for h in self.q:
            for n in self.list:
                for j in n['rects']:
                    if j.collidepoint(h.where_walk_enemy.center):
                        n['enemys'].append(h)
    def zapusk(self):
        for q in self.list:
            q['go_sleep'] = pygame.event.custom_type()
            pygame.time.set_timer(q['go_sleep'], q['time_sleep']*1000,1)
    def controller(self,event,fly_finish_callback):
        for u in event:
            h=self.finder(u)
            if None is h:
                continue
            for l in h['enemys']:
                if l==self.list[-1]['enemys'][-1]:
                    l.go_free_fly(h['points'].copy(), h['enemys'],fly_finish_callback)
                else:
                    l.go_free_fly(h['points'].copy(),h['enemys'])
    def finder(self,u):
        for h in self.list:
            if h['go_sleep'] == u.type:
                return h




