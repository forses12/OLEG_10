import pygame, model
def comtrol():

    event=pygame.event.get()
    model.p.control(event)
    model.q.control(event)
    model.w.control(event)
    for e in event:
        if e.type==pygame.QUIT:
            exit()
        if e.type==pygame.KEYDOWN and e.key==pygame.K_TAB:
            model.event_for_debug=not model.event_for_debug
        if e.type==pygame.KEYDOWN and e.key==pygame.K_q:
            model.normal_paint=not model.normal_paint
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            model.q.walk = not model.q.walk
            model.w.walk = not model.w.walk
        if e.type==pygame.KEYDOWN and e.key==pygame.K_s:
            model.q.go_rotate(45)
        if e.type==pygame.KEYDOWN and e.key==pygame.K_d:
            model.q.go_rotate(111)








