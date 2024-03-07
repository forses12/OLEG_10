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
            a=[
                {
                    'x': 50,
                    'y': 50,
                    'speed': 3,
                    'angle': -5
                }
                ,
                {
                    'x': 150,
                    'y':400,
                    'speed':3,
                    'angle':-5
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
                    'x': 300,
                    'y': 200,
                    'speed': 3,
                    'angle': -5
                }
                ,
                {
                    'mode': 'walk',
                    'speed': 3,
                    'angle': -5

                }]
            b=[]
            for h in range(len(a)):
                b.append(a[h].copy())
            for h in range(len(b)):
                if 'x' in a[h].keys():
                    b[h]['x']=1000-a[h]['x']
            for j in range(len(model.q)):
                if model.q[j].where[0]<500:
                    model.q[j].go_free_fly(a.copy())
                else:
                    model.q[j].go_free_fly(b.copy())










