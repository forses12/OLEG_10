import math

import pygame, math_utils, random


class Enemy:
    def __init__(self, who, where,  how_many_more, y, left, right, step_delay, step, speedtp):
        self.who = who
        self.image1 = self.who
        self.image2 = self.who.replace('1', '2')
        self.where = where
        self. how_many_more= how_many_more

        self.images = pygame.image.load(self.image1)
        self.images1 = pygame.image.load(self.image2)
        self.size = [self.images.get_width() * how_many_more, self.images.get_height() *  how_many_more]
        self.image = pygame.transform.scale(self.images, self.size)
        self.image_finale = pygame.transform.scale(self.images, self.size)

        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(where, self.image_finale.get_size())
        self.rect.center = where

        self.p = pygame.event.custom_type()
        pygame.time.set_timer(self.p, step_delay)
        self.m = pygame.event.custom_type()
        pygame.time.set_timer(self.m, 10)
        self.l = pygame.event.custom_type()
        pygame.time.set_timer(self.l, 10)
        self.changed_picture = True

        self.leftx = left
        self.rightx = right
        self.speedx = step
        self.walk = False
        self.angle = 0
        self.how_many_rotate = 0
        self.let_go_tp = False
        self.speedtp = speedtp
        self.xy_fly = []
        self.fly = False
        self.let_go_rotate = True
        self.where_walk_enemy = self.rect.copy()
        self.where_walk_enemy.center = [left + 0.5 * (right - left), y]
        self.shot_callback=None
    def _a_che(self):
        if self.changed_picture:
            image = self.images1
            self.size = [self.images1.get_width() * self.how_many_more, self.images1.get_height() * self.how_many_more]
        else:
            image = self.images
            self.size = [self.images.get_width() * self.how_many_more, self.images.get_height() * self.how_many_more]
        self.changed_picture = not self.changed_picture

        self._remake_center(self.size)

        self.image_finale = pygame.transform.scale(image, self.size)

    def sozdowatel(self):
        self.screen.blit(self.image_finale, self.rect)

    def _remake_center(self, size):
        center = self.rect.center
        self.rect.size = size
        self.rect.center = center

    def go_walk(self):
        self.walk = True
        self.let_go_rotate = False

    def sozdowatel_debug(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 2)
        pygame.draw.rect(self.screen, [255, 0, 255], self.where_walk_enemy, 2)
        pygame.draw.line(self.screen, [255, 0, 255], [self.leftx, self.rect.top], [self.leftx, self.rect.bottom], 2)
        pygame.draw.line(self.screen, [255, 0, 255], [self.rightx, self.rect.top], [self.rightx, self.rect.bottom], 2)
        for a in self.xy_fly:
            if 'x' in a.keys():
                pygame.draw.circle(self.screen, [255, 0, 0], [a['x'], a['y']], 3)

    def control(self, event):
        for i in event:
            if i.type == self.p:
                self._go()
            if i.type == self.p and self.walk:
                self.real_walk()
            if i.type == self.m and self.let_go_rotate:
                self._go_rotate()
            if i.type == self.l and self.let_go_tp:
                self._tp()
                self.lot_of_tp(self.xyz)
            if i.type == self.l and self.fly:
                self.free_fly()

    def _go(self):

        self.where_walk_enemy.centerx += self.speedx
        self._a_che()
        if self.where_walk_enemy.right >= self.rightx and self.speedx > 0:
            self.where_walk_enemy.right = self.rightx
            self.speedx = -self.speedx
        elif self.where_walk_enemy.left <= self.leftx and self.speedx < 0:
            self.where_walk_enemy.left = self.leftx
            self.speedx = -self.speedx

    def real_walk(self):
        self.rect.center = self.where_walk_enemy.center

    def start_go_rotate(self, angle):
        self.walk = False
        self.angle = angle
        self.let_go_rotate = True

    def lot_of_tp(self, xy):
        if self.let_go_tp == False and len(xy) != 0:
            self.go_tp(xy[0])
            self.xyz = xy
            del xy[0]

    def _rotate(self, znak):
        self.image_finale = pygame.transform.rotate(self.image, -self.how_many_rotate)
        self.how_many_rotate += znak * 1
        self._remake_center(self.image_finale.get_size())

    def _go_rotate(self):
        if int(self.how_many_rotate) < self.angle:
            self._rotate(1)
        elif int(self.how_many_rotate) > self.angle:
            self._rotate(-1)
        else:
            self.let_go_rotate = False

    def go_tp(self, xy):
        self.walk = False
        self.xy = xy
        distanse = math.dist(self.rect.center, xy)

        d_xy = [xy[0] - self.rect.centerx, xy[1] - self.rect.centery]
        procent = self.speedtp / distanse
        self.tp_speedxy = [d_xy[0] * procent, d_xy[1] * procent]
        self.tp_rect = [self.rect.centerx, self.rect.centery]
        self.let_go_tp = True

    def _tp(self):
        if (self.tp_speedxy[0] > 0 and self.rect.centerx < self.xy[0]) \
                or (self.tp_speedxy[0] < 0 and self.rect.centerx > self.xy[0]):

            self.tp_rect[0] += self.tp_speedxy[0]
            self.tp_rect[1] += self.tp_speedxy[1]

            self.rect.centerx = self.tp_rect[0]
            self.rect.centery = self.tp_rect[1]
        else:
            self.let_go_tp = False
            self.rect.center = self.xy

    def spavn(self,f):
        xy=[self.xy_fly[0]['x'], self.xy_fly[0]['y']]
        a=math_utils.get_angle_by_point(xy.copy(),self.rect.center)
        m= math.dist(self.rect.center, xy)
        for d in f:
            if d is self:
                continue
            m += 70
            g=math_utils.get_point_by_angle(xy.copy(),a,m)
            d.rect.center=g




    def go_free_fly(self, xy,q=None,fly_finish_callback=None):
        self.fly = True
        self.let_go_rotate = True
        self.walk = False

        self.xy_fly = xy
        self.fly_finish_callback=fly_finish_callback
        if q is not None and self is q[0]:
            q[0].spavn(q)

    def free_fly(self):
        if self.rect.top >= 700:
            self.rect.bottom = 0
        if 'mode' in self.xy_fly[0].keys() and self.xy_fly[0]['mode'] == 'walk':
            self.xy_fly[0]['x'] = self.where_walk_enemy.centerx
            self.xy_fly[0]['y'] = self.where_walk_enemy.centery

        self.how_many_rotate = self.how_many_rotate % 360
        m = math.dist(self.rect.center, [self.xy_fly[0]['x'], self.xy_fly[0]['y']])
        u = 360 - math_utils.get_angle_by_point(self.rect.center, [self.xy_fly[0]['x'], self.xy_fly[0]['y']])
        if callable(self.shot_callback) and len(self.xy_fly)==3:
            self.shot_callback(self)
            self.shot_callback=None
        if  not self.rect.collidepoint(self.xy_fly[0]['x'],self.xy_fly[0]['y']):
            self.let_go_rotate = True
            xy_tp = math_utils.get_point_by_angle([*self.rect.center], -self.how_many_rotate, self.xy_fly[0]['speed'])

            self.rect.center = xy_tp
            o = u - 360
            if self.how_many_rotate + abs(self.xy_fly[0]['angle']) * 2 >= u \
                    and self.how_many_rotate - abs(self.xy_fly[0]['angle'] * 2) <= u \
                    or self.how_many_rotate - abs(self.xy_fly[0]['angle'] * 2) <= o:
                self.how_many_rotate = u
            else:
                self.how_many_rotate += self.xy_fly[0]['angle']


        elif len(self.xy_fly) > 1:
            del self.xy_fly[0]


        else:

            self.fly = False
            self.walk = True
            self.let_go_rotate= True
            if callable(self.fly_finish_callback):
                self.fly_finish_callback()

    def attack(self,player,shot_callback=None):
        self.go_free_fly(self._math_attack(player))
        self.shot_callback=shot_callback

    def _math_attack(self,player):

        points= [{
            'speed': 3,
            'angle': 5
        }
            ,
            {
                'speed': 3,
                'angle': 5
            }
            ,
            {
                'speed': 3,
                'angle': -5
            }
            ,
            {
                'speed': 3,
                'angle': -5
            }
            ,
            {
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
        step_y=(600-self.rect.centery)/5
        for j in range(len(points)):
            if j==0:
                random_x=random.randint(self.rect.centerx-200,self.rect.centerx+200)
                points[j]['x']=random_x
                points[j]['y'] = self.rect.centery + step_y * (j + 1)


            elif 'mode' not in points[j] and j!=3 and j!=4:
                random_x=random.randint(points[j-1]['x']-200,points[j-1]['x']+200)
                points[j]['x'] = random_x
                points[j]['y'] = self.rect.centery + step_y * (j + 1)
            elif j==3:
                points[j]['x'] = player.rect.centerx
                points[j]['y'] = player.rect.centery
            elif j==4:
                points[j]['x'] = points[j-1]['x']
                points[j]['y'] = 700+self.rect.size[1]/2



        return points


        # if self.how_many_rotate!=angle:
        #
        #     self.image_finale=pygame.transform.rotate(self.image, -angle)
        #     self.how_many_rotate=angle
        #     self.remake_center(self.image_finale.get_size())
