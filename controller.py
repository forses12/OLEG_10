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
            for h in model.k.list:
                for l in h['enemys']:
                    l.go_free_fly(h['points'],h['enemys'])




