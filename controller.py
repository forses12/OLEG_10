import pygame, model

def comtrol():
    event=pygame.event.get()
    model.p.control(event)
    model.q.go(event)
    model.w.go(event)
    for e in event:
        if e.type==pygame.QUIT:
            exit()
        if e.type==pygame.KEYDOWN and e.key==pygame.K_TAB:
            model.event_for_debug=not model.event_for_debug

