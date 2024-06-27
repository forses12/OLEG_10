import pygame

class X():
    def __init__(self,where,how_many,width,image,dist=0,l_or_r=-1):
        """
        :param l_or_r: l=1 r=-1
        """
        self.screen=pygame.display.get_surface()
        self.image = image
        image = pygame.image.load(self.image)
        self.size = [width,image.get_height()*width/image.get_width()]
        self.image = pygame.transform.scale(image, self.size)
        self.where=where
        self.how_many=how_many
        self.dist=dist
        self.l_or_r=l_or_r
    def painting(self):
        for x in range(self.how_many):
            self.screen.blit(self.image,[self.where[0]+self.l_or_r*x*(self.size[0]+self.dist),self.where[1]])