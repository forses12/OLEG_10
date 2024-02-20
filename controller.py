import pygame, model,random

def comtrol():

    event=pygame.event.get()
    model.p.control(event)
    for a in model.q:
        a.control(event)

    for e in event:
        if e.type==pygame.QUIT:
            exit()
        if e.type==pygame.KEYDOWN and e.key==pygame.K_TAB:
            model.event_for_debug=not model.event_for_debug
        if e.type==pygame.KEYDOWN and e.key==pygame.K_q:
            model.normal_paint=not model.normal_paint
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:

            model.q[0].go_walk()


        if e.type==pygame.KEYDOWN and e.key==pygame.K_s:
            model.q[0].start_go_rotate(0)

        if e.type==pygame.KEYDOWN and e.key==pygame.K_d:
            model.q[0].start_go_rotate(111)
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            model.q[0].lot_of_tp([[random.randint(100,900),random.randint(100,600)],
                              [random.randint(100, 900), random.randint(100, 600)]])
        if e.type == pygame.KEYDOWN and e.key == pygame.K_g:
            model.q[0].go_free_fly([
                {
                    'x': 95,
                    'y':100,
                    'speed':1.5,
                    'angle':3
                }
                ,
                {
                    'x': 500,
                    'y': 500,
                    'speed': 3,
                    'angle': -3
                }
            ])








