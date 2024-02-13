import math

import pygame, math_utils


class Enemy:
    def __init__(self, who, where,left,right,step_delay,step,speedtp):
        self.who = who
        self.image1 = self.who
        self.image2 = self.who.replace('1', '2')
        self.where=where

        self.images = pygame.image.load(self.image1)
        self.images1 = pygame.image.load(self.image2)
        self.size = [self.images.get_width() * 4, self.images.get_height() * 4]
        self.image = pygame.transform.scale(self.images,    self.size )
        self.image_finale = pygame.transform.scale(self.images,   self.size )

        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(where, self.image_finale.get_size())

        self.p = pygame.event.custom_type()
        pygame.time.set_timer(self.p, step_delay )
        self.m = pygame.event.custom_type()
        pygame.time.set_timer(self.m, 10)
        self.l = pygame.event.custom_type()
        pygame.time.set_timer(self.l, 10)
        self.changed_picture = True

        self.leftx=left
        self.rightx=right
        self.speedx=step
        self.walk=True
        self.angle=0
        self.how_many_rotate=0
        self.let_go_tp=False
        self.speedtp=speedtp
        self.fly=False
    def _a_che(self):
        if self.changed_picture:
            image = self.images1
            self.size = [self.images1.get_width() * 4, self.images1.get_height() * 4]
        else:
            image = self.images
            self.size = [self.images.get_width() * 4, self.images.get_height() * 4]
        self.changed_picture = not self.changed_picture

        self._remake_center(self.size)

        self.image_finale = pygame.transform.scale(image, self.size)

    def sozdowatel(self):
        self.screen.blit(self.image_finale, self.rect)
    def _remake_center(self,size):
        center=self.rect.center
        self.rect.size = size
        self.rect.center=center
    def go_walk(self):
         self.walk=True


    def sozdowatel_debug(self):
        pygame.draw.rect(self.screen, [255, 255, 255], self.rect, 2)
        pygame.draw.line(self.screen,[255,0,255],[self.leftx,self.rect.top],[self.leftx,self.rect.bottom],2)
        pygame.draw.line(self.screen,[255,0,255],[self.rightx,self.rect.top],[self.rightx,self.rect.bottom],2)


    def control(self, event):
        for i in event:
            if i.type == self.p and self.walk:
                self._go()
            if i.type == self.m:
                self._go_rotate()
            if i.type == self.l  and self.let_go_tp :
                self._tp()
                self.lot_of_tp(self.xyz)
            if i.type == self.l and self.fly:
                self.free_fly()


    def _go(self):

            self.rect.centerx += self.speedx
            self._a_che()
            if self.rect.right >= self.rightx and self.speedx > 0:
                self.rect.right = self.rightx
                self.speedx = -self.speedx
            elif self.rect.left <= self.leftx and self.speedx < 0:
                self.rect.left = self.leftx
                self.speedx = -self.speedx
    def start_go_rotate(self,angle):
        self.walk = False
        self.angle=angle
    def lot_of_tp(self,xy):
        if self.let_go_tp==False and len(xy)!=0:
            self.go_tp(xy[0])
            self.xyz=xy
            del xy[0]





    def _rotate(self,znak):
        self.image_finale = pygame.transform.rotate(self.image, -self.how_many_rotate)
        self.how_many_rotate += znak*1
        self._remake_center(self.image_finale.get_size())
    def _go_rotate(self):
        if self.how_many_rotate<self.angle:
            self._rotate(1)
        elif self.how_many_rotate>self.angle:
            self._rotate(-1)

    def go_tp(self, xy):
        self.walk=False
        self.xy=xy
        distanse=math.dist(self.rect.center,xy)

        d_xy=[xy[0]-self.rect.centerx,xy[1]-self.rect.centery]
        procent=self.speedtp/distanse
        self.tp_speedxy=[d_xy[0]*procent,d_xy[1]*procent]
        self.tp_rect = [self.rect.centerx, self.rect.centery]
        self.let_go_tp=True

    def _tp(self):
        if (self.tp_speedxy[0] > 0 and self.rect.centerx < self.xy[0]) \
                or (self.tp_speedxy[0] < 0 and self.rect.centerx > self.xy[0]):
            print(self.rect.center)
            print(self.tp_speedxy)
            self.tp_rect[0]+=self.tp_speedxy[0]
            self.tp_rect[1]+=self.tp_speedxy[1]


            self.rect.centerx=self.tp_rect[0]
            self.rect.centery=self.tp_rect[1]
            print(self.rect.center)
            print('-------------------------------')
        else:
            self.let_go_tp=False
            self.rect.center=self.xy

    def go_free_fly(self,xy):
        self.fly=True
        self.walk=False
        self.xy_fly=xy

    def free_fly(self):
        self.how_many_rotate=self.how_many_rotate%360
        u=360-math_utils.get_angle_by_point(self.rect.center,[self.xy_fly[0]['x'],self.xy_fly[0]['y']])
        print(self.how_many_rotate,u)
        if self.how_many_rotate!=u:
            xy_tp = math_utils.get_point_by_angle([*self.rect.center], -self.how_many_rotate, self.xy_fly[0]['speed'])
            self.rect.center=xy_tp
            if self.how_many_rotate<u:
                self.how_many_rotate+=self.xy_fly[0]['angle']
            else:
                self.how_many_rotate -= self.xy_fly[0]['angle']






        # if self.how_many_rotate!=angle:
        #
        #     self.image_finale=pygame.transform.rotate(self.image, -angle)
        #     self.how_many_rotate=angle
        #     self.remake_center(self.image_finale.get_size())