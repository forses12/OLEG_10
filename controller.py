import pygame, model,random,bullet

p = pygame.event.custom_type()

you_can=True
h= pygame.event.custom_type()
def start_timer_attack():
    pygame.time.set_timer(h, 1000)

def comtrol():
    global you_can

    event=pygame.event.get()
    model.p.control(event)
    model.k.controller(event,start_timer_attack)
    for a in model.q:
        a.control(event)
    for s in model.s:
        s.control(event)
    print(pygame.mouse.get_pressed())
    if pygame.mouse.get_pressed()[0] and you_can:
        model.h.append(bullet.Bullet(model.q, model.p, model.h))
        you_can = False
        pygame.time.set_timer(p, 300, 1)
    for e in event.copy():
        if e.type == p:
            you_can=True

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
        if  e.type == h:
            model.q[random.randint(0,len(model.q)-1)].attack(model.p)
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            for a in range(len(model.q)):
                model.q[a].lot_of_tp([[random.randint(100,900),random.randint(100,600)],
                                  [random.randint(100, 900), random.randint(100, 600)]])




