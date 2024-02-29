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
            for a in range(len(model.q)):
                model.q[a].lot_of_tp([[random.randint(100,900),random.randint(100,600)],
                                  [random.randint(100, 900), random.randint(100, 600)]])
        if e.type == pygame.KEYDOWN and e.key == pygame.K_g:
            for a in range(len(model.q)):
                model.q[a].go_free_fly([
                    {
                        'x': 50,
                        'y': 50,
                        'speed': 4,
                        'angle': -3
                    }
                    ,
                    {
                        'x': 150,
                        'y':400,
                        'speed':4,
                        'angle':-3
                    }
                    ,
                    {
                        'x': 375,
                        'y': 500,
                        'speed': 3,
                        'angle': -1
                    }
                    ,
                    {
                        'x': 480,
                        'y': 400,
                        'speed': 4,
                        'angle': -1
                    }
                    ,
                    {
                        'x': 300,
                        'y': 200,
                        'speed': 4,
                        'angle': -5
                    }
                    ,
                    {
                        'mode': 'walk',
                        'speed': 4,
                        'angle': -5

                    }
                ])








