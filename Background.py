import pygame

class Background():
    def __init__(self, screen):
        self.screen = screen
        self.bgimage = pygame.image.load('images/space_black.png')
        self.rectBGimg = self.bgimage.get_rect()
        self.bgimage = pygame.transform.scale(self.bgimage, (int(800 / self.rectBGimg.width * self.rectBGimg.width), int(600 / self.rectBGimg.width * self.rectBGimg.height)))
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = self.rectBGimg.height
        self.bgX2 = 0

        self.movingUpSpeed = 5

    def update(self):
        self.bgY1 += self.movingUpSpeed
        self.bgY2 += self.movingUpSpeed
        if self.bgY1 >= self.rectBGimg.height:
            self.bgY1 = -self.rectBGimg.height
        if self.bgY2 >= self.rectBGimg.height:
            self.bgY2 = -self.rectBGimg.height

    def render(self):
        self.screen.blit(self.bgimage, (self.bgX1, self.bgY1))
        self.screen.blit(self.bgimage, (self.bgX2, self.bgY2))