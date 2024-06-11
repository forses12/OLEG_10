import math
import pygame, math_utils, enemy, random, enemy_bullet

BIG_GREEN1 = 'big_green1.png'
BUTTERFLY_RED1 = 'butterfly_red1.png'
FLY_BLUE1 = 'fly_blue1.png'
h= pygame.event.custom_type()

class Level:
    def __init__(self, q,p,h):
        self.screen = pygame.display.get_surface()
        self.q = q
        self.h=h
        self.p=p
        self.v=3
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
                      'time_sleep': 7,
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
                      'time_sleep': 7,
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
                      'time_sleep': 7,
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
                      'time_sleep': 7,
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
                      'time_sleep':7 ,
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

    def start_timer_attack(self):
        if self.can_attack(1):
            pygame.time.set_timer(h, 1000)

    def can_attack(self,lm):
        l = 0
        for k in self.q:
            if k.fly:
                l += 1
                if l >= lm:
                    return False
        return True
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

    def controller(self,event):
        for u in event:
            if u.type == h and len(self.q) > 0 and self.can_attack(1):
                random1=random.randint(0, len(self.q) - 1)
                d=random.randint(1,self.v)
                self.v=self.v-1 if d!=1 else self.v+1
                a=self.enemy_callback if d==1 else None
                self.q[random1].attack(self.p,a )
            v=self.finder(u)
            if None is v:
                continue
            for l in v['enemys']:
                l.go_free_fly(v['points'].copy(), v['enemys'],self.start_timer_attack)

    def finder(self,u):
        """
        возврашяет словарь с наступившим таймером
        """
        for h in self.list:
            if h['go_sleep'] == u.type:
                return h
    def enemy_callback(self,enemy):
        k=enemy_bullet.Enemy_bullet(self.p,enemy,self.h)
        self.h.append(k)
        print(len(self.h))




