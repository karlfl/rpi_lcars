import pygame
from pygame.locals import *
from pygame.sprite import DirtySprite, LayeredDirty

from ui import colours
from ui.widgets.lcars_widgets import LcarsBlockLarge, LcarsBlockMedium, LcarsBlockSmall, LcarsText

# init
pygame.init()
screenSurface = pygame.display.set_mode((480, 320))

class PpuiImage(DirtySprite):
    """Image sprite"""
    
    def __init__(self, imagepath):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(imagepath).convert()
        self.rect = self.image.get_rect()

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def applyColour(self, colour):
        """Very simple colour substitution"""
        for x in range(0, self.rect.width):
            for y in range(0, self.rect.height):
                pixel = self.image.get_at((x, y)).r
                if (pixel > 50):
                    self.image.set_at((x, y), colour)


# create sprites
bg = PpuiImage("assets/lcars_screen_sm.png")
button = PpuiImage("assets/button.png")
button.applyColour((255, 204, 153))

# add sprites to layer
sprites = LayeredDirty()
sprites.add(bg)
# sprites.add(button)
sprites.add(LcarsText(colours.BLACK, (15, 20), "LCARS 105"),layer=1)
sprites.add(LcarsText(colours.ORANGE, (0, 100), "ENGINEERING CONTROL", 2),layer=1)
sprites.add(LcarsText(colours.BLACK, (145, 20), "LIGHTS"),layer=1)
sprites.add(LcarsText(colours.BLACK, (211, 20), "CAMERAS"),layer=1)
sprites.add(LcarsText(colours.BLACK, (249, 20), "ENERGY"),layer=1)

# event loop
while pygame.display.get_init():
    sprites.draw(screenSurface)
    pygame.display.update()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or \
            event.type == KEYUP:
            pygame.quit()
            break
        
        if (event.type == MOUSEMOTION):
            # move button around as mouse moves (or touch-drag)
            button.rect.left = event.pos[0]
            button.rect.top = event.pos[1]
            button.dirty = 1

