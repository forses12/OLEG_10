import pygame, model

def comtrol():
    event=pygame.event.get()
    model.p.control(event)
    for e in event:
        if e.type==pygame.QUIT:
            exit()