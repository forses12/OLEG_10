import pygame, model, random, bullet, enemy_bullet

import enemy_bullet
pygame.key.set_repeat(100)
p = pygame.event.custom_type()

you_can = True


def comtrol():
    global you_can
    event = pygame.event.get()
    model.p.control(event)
    model.k.controller(event)
    for a in model.q:
        a.control(event)
    for s in model.s:
        s.control(event)
    for e in event.copy():
        if (pygame.mouse.get_pressed()[0] or
            (e.type == pygame.KEYDOWN and \
             (e.key == pygame.K_z or e.key == pygame.K_x)
            )) and \
                you_can:
            model.h.append(bullet.Bullet(model.q, model.p, model.h))
            you_can = False
            pygame.time.set_timer(p, 300, 1)
        if e.type == p:
            you_can = True

        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYUP and e.key == pygame.K_TAB:
            model.event_for_debug = not model.event_for_debug
        if e.type == pygame.KEYUP and e.key == pygame.K_q:
            model.normal_paint = not model.normal_paint

        if e.type == pygame.KEYUP and e.key == pygame.K_a:
            model.q[0].go_walk()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            model.q[0].start_go_rotate(0)

        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            model.q[0].start_go_rotate(111)
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            k = enemy_bullet.Enemy_bullet(model.p, model.q[7], model.h)
            model.h.append(k)
