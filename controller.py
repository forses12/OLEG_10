import pygame, model

def comtrol():
    event=pygame.event.get()
    for e in event:
        if e.type==pygame.QUIT:
            exit()