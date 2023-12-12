import pygame,player

p=player.Player([600,500])
p.sozdowatel()
event_for_debug=False
def model():
    debug()
def debug():
    if event_for_debug:
        p.sozdowatel_debug()

