# Python file containing classes to make instances of UI objects such as buttons
"""
v 1.0
 - Normal and Image static buttton class
 - Normal static fonts class
"""
import pygame as pg
pg.init()
if not pg.get_init():
    print("There was something wrong with the program *>*")
    quit()

# Loads general data
# Default fonts
DefaultFont = "freesansbold.ttf"

# --- Text generator ---
"""
Font class takes various arguments to create and instance of Text and rectangle with their attributes
This simplifies the use of fonts throughout the game after creation
"""
class TextGen:
    def __init__(self, Size, Text, TextColour, BGColour, MidPosX, MidPosY, Antialias = True, Center = True):
        self.font = pg.font.Font(DefaultFont, Size)
        self.Text = self.font.render(Text, Antialias, TextColour, BGColour)
        self.rect = self.Text.get_rect()
        if Center:
            self.rect.center = (MidPosX, MidPosY)
        else:
            self.rect[0] = MidPosX
            self.rect[1] = MidPosY
        self.originX = self.rect[0]
        self.originY = self.rect[1]
        self.endX = self.originX + self.rect[2]
        self.endY = self.originY + self.rect[3]

    # Renders the Text onto the screen
    def Render(self, Window):
        Window.blit(self.Text, self.rect)

# --- Button Text generator ---
# Works similarly to the font generator but has interactivity by checking whether there is input within its hit box
class TextButton:
    def __init__(self, Size, Text, Antialias, defColour, MidPosX, MidPosY):
        self.font = pg.font.Font(DefaultFont, Size)
        self.Text = self.font.render(Text, Antialias, defColour[1], defColour[0])
        self.rect = self.Text.get_rect()
        self.rect.center = (MidPosX, MidPosY)
        self.originX = self.rect[0]
        self.originY = self.rect[1]
        self.endX = self.originX + self.rect[2]
        self.endY = self.originY + self.rect[3]

    # Renders the button onto the screen
    def render(self, Window):
        Window.blit(self.Text, self.rect)

    # Checks whether the input is within the button parameters
    def positionCheck(self, MousePos):
        if (self.originX < MousePos[0] < self.endX) and (self.originY < MousePos[1] < self.endY):
            return True

    def changeText(self, newText):
        self.Text = newText

# --- Button Image generator ---
# Works similarly but Text attributes are replaced with an Image
class ImgButton:
    def __init__(self, Image, MidPosX, MidPosY):
        self.Image = Image
        self.rect = self.Image.get_rect()
        self.rect.center = (MidPosX, MidPosY)
        self.OriginX = self.rect[0]
        self.OriginY = self.rect[1]
        self.EndX = self.OriginX + self.rect[2]
        self.EndY = self.OriginY + self.rect[3]

    # Renders the button onto the screen
    def Render(self, Window):
        Window.blit(self.Image, self.rect)

    # Checks whether the input is within the button parameters
    def PosCheck(self, MousePos):
        if (self.OriginX < MousePos[0] < self.EndX) and (self.OriginY < MousePos[1] < self.EndY):
            return True