import pygame,player,enemy

p=player.Player([600,500])

q=(enemy.Enemy('images/flies/butterfly_red1.png',[500,-40],100,90,300,500,30,1.5),
enemy.Enemy('images/flies/butterfly_red1.png',[550,-60],100,90,370,500,30,1.5),
enemy.Enemy('images/flies/butterfly_red1.png',[600,-80],100,90,440,500,30,1.5),
enemy.Enemy('images/flies/butterfly_red1.png',[650,-100],100,90,510,500,30,1.5),
enemy.Enemy('images/flies/butterfly_red1.png',[700,-120],100,90,580,500,30,1.5),
)
q[0].walk=False

event_for_debug=False
normal_paint=True
def model():
    pass

