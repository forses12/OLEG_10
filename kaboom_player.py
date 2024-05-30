import kaboom


images = [kaboom.make_image('images/player/player_burst1.png'),
          kaboom.make_image('images/player/player_burst2.png'),
          kaboom.make_image('images/player/player_burst3.png'),
          kaboom.make_image('images/player/player_burst4.png'),
          kaboom.make_image('images/flies/enemy_burst5.png')]
class Kaboom_player(kaboom.Kaboom):
    def __init__(self,p):
        kaboom.Kaboom.__init__(self,p.rect.center)
        self.images=images.copy()