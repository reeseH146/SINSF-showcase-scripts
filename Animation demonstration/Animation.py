# A series of animations the program can play which can be played
import pygame as pg
from pygame.locals import *
pg.init()
import PGUI

# --- Animation class ---

"""
A class which allows updating of sprite sheet frame.
Used in place of cycling images since it is easier to manage sprite sheets in files rather than many images with similar names/variants.
A class allows it to be applied to different sprite sheets and track. 
Only tested on png/jpeg in animation sheet format. 
Max frame can be float but complicated and unnecessary.
Frames are all fixed length in duration

Commands : 
 - AnimatedSprite = Animation(SSheet, Loc, Size, Speed, Increment, MaxFrame)
 - AnimatedSprite.AniUpdate() # Just updates the frame count of the sprite and frame if frame count is high enough
 - AnimatedSprite.LocUpdate("{w/a/s/d}") # Updates the location self.speed distance depending on direction input
 - AnimatedSprite.LocUpdate("", False, [x, y]) # False flag changes default location update type to update by cord and not direction
 - AnimatedSprite.SizeUpdate(Scale) # Increases the size of the animation by a given scale, a min and max range will limit the extent of this transformation

Main
 - Creates a surface
 - Creates counter, increment, speed, spritesheet, sizes and location variable to keep track of animation attributes
 
Animation update
 - Updates the counter
 - Updates the image on the surface according to the counter

Position update
 - Updates the position depending on direction/position input
 - Updates the position of surface on the display
"""
"""
 - Animation object is created with necessary parses
 - Animation.AniUpdate() called to update frame, typically every frame/loop
 - Animation.LocUpdate() called to update location, based on user input or program calculated location 
"""
class Animation:
    def __init__(self, SSheet, Loc : [], Size : (), ScaleLim : (), Speed : int, Increment : float, MaxFrame : int, Move = False):
        # SSheet and attributes
        self.SSheet = SSheet
        self.Loc = Loc
        self.Size = Size
        self.ScaleLim = ScaleLim
        self.Move = Move
        # Animation attributes
        self.Speed = Speed
        self.Frame = 0
        self.Increment = Increment
        self.MaxFrame = MaxFrame
        self.Image = pg.Surface(self.Size)
        self.rect = self.Image.get_rect()

    def AniUpdate(self):
        """
        Blits section of SSheet onto Image.
        Area(LeftX, TopY, XWideToRight, YTallToDown).
        LeftX is the TL X of rect, which a sample of SSheet is taken. Frame * Size calculates position along the SSheet.
        TopY is the TL Y of rect, which a sample of SSheet is taken.
        XWideToRight and YTallToDown are height and width of rect.
        """
        self.Image.blit(self.SSheet, (0, 0), (self.Size[0] * int(self.Frame), 0, self.Size[0], self.Size[1]))
        self.Frame += self.Increment # Increments frame
        if self.Frame > self.MaxFrame: # Checks if frame is above total sprites and resets if so
            self.Frame = 0
        # Updates Window and animation frame
        Window.fill((0, 0, 0))
        Window.blit(self.Image, self.rect)

    def LocUpdate(self, Direction = "", UpdateByDirection = True, Position = (0, 0)):
        if self.Move:
            if UpdateByDirection:
                if Direction == "w": # Updates vertical position
                    self.Loc[1] -= self.Speed
                elif Direction == "a": # Updates horizontal position
                    self.Loc[0] -= self.Speed
                elif Direction == "s": # Updates vertical position
                    self.Loc[1] += self.Speed
                elif Direction == "d": # Updates horizontal position
                    self.Loc[0] += self.Speed
            else:
                self.Loc = Position
            # Updates Window and animation in new position
            self.rect.center = (self.Loc[0], self.Loc[1])
            Window.fill((0, 0, 0))
            Window.blit(self.Image, self.rect)

    def SizeUpdate(self, Scale):
        if self.ScaleLim[0] <= Scale <= self.ScaleLim[1]:
            self.size = (self.Size[0] * Scale, self.Size[1] * Scale)
            #self.Image = pg.Surface(self.size)
            self.SSheet = pg.transform.scale_by(self.SSheet, Scale, self.Image)


"""---"""

# --- Main Menu ---
def MainMenu():
    # Loads the main menu visual assets and interactive assets
    Window.fill(MAINCOLOUR)
    pg.draw.rect(Window, SUBCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10)
    """
    MenuTitle.render()
    Tutorial.render()
    ATestBTN.render()
    AWaveBTN.render()
    ABounceBallBTN.render()
    ATrigWaveBTN.render()
    """
    while True:
        # Loops through the event queue checking for any events, mainly user input
        for event in pg.event.get():
            # Quits the game if user clicks on close window button (X)
            if (event.type == QUIT) or (pg.key == K_ESCAPE):
                Running = False
                pg.quit()
                print(f"{'':-^42}\n{' Program closed : Thank you for playing ':-^42}\n{'':-^42}") # Cursed mono line alignment
                quit()
            # Checks mouse button has been lifted and that it is the left mouse button
            elif (event.type == MOUSEBUTTONDOWN) and (pg.mouse.get_pressed()[0]):
                MousePosition = pg.mouse.get_pos()
                print(2)

        pg.display.update()
        Clock.tick(60)

# --- Main Game ---
def MainGame():
    Window.fill(MAINCOLOUR)
    pg.draw.rect(Window, SUBCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10)
    ## Makes some checks and updates the window to show information to the user



    Running = True
    while Running:
        # Loops through the event queue checking for any events, mainly user input
        for event in pg.event.get():
            # Grabs a list of the state of all possible events
            Events = pg.key.get_pressed()
            # Quits the game if user clicks on close window button (X)
            if event.type == QUIT:
                Running = False
                pg.quit()
                print(f"{'':-^42}\n{' Program closed : Thank you for playing ':-^42}\n{'':-^42}") # Cursed mono line alignment
                quit()

            # Returns to MainMenu is ESC is pressed
            if Events[K_ESCAPE]:
                MainMenu()
            # Changes animation speed if user clicks Left/Right Arrow
            elif Events[K_LEFT]: # Decrease speed
                pass
            elif Events[K_RIGHT]: # Increase speed
                pass
            # Changes size of animation in place with Up/Down Arrow
            elif Events[K_UP]:
                pass
            elif Events[K_DOWN]:
                pass
            # Resets position of animation to centre
            elif Events[K_SPACE]:
                pass

        # Updates the sprite


    pg.display.update()
    Clock.tick(60)

# --- Main ---
print(f"{'':-^42}\n{' Program loaded : Please enjoy playing  ':-^42}\n{'':-^42}") # Cursed mono line alignment

## Default values making it easier to track and reuse variables across this script
WINSIZE = (1920 * 0.65, 1080 * 0.65)
Clock = pg.time.Clock()
MAINCOLOUR = (255, 191, 70)
SUBCOLOUR = (87, 87, 91)
ACCENTCOLOUR = (147, 147, 158)
TEXTCOLOUR = (255, 255, 255)

## Game loading screen while other parts of the program load, there are some parts that should be in other section but is necessary for the loading screen to work
Icon = pg.image.load("SpriteSheets\KES.png") # Loads image used for program icon
WellcomeMsg = PGUI.TextGen(50, "Welcome to the animation demonstration", TEXTCOLOUR, SUBCOLOUR, WINSIZE[0] // 2, WINSIZE[1] // 2) # Centre of window
pg.display.set_icon(Icon) # Sets loaded image of KES to window icon
pg.display.set_caption("Animation Demonstration") # Sets window caption of what this program is to the user
Window = pg.display.set_mode(WINSIZE) # Creates the window
pg.Surface.fill(Window, MAINCOLOUR) # Fills window with a background colour
pg.draw.rect(Window, ACCENTCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10) # Draws an empty rectangle as the window border
WellcomeMsg.render(Window) # Places a welcome message onto the window for the user
pg.display.update() # Updates the differences in the window since last update/creation so user can see changes
pg.time.wait(600) # Waits 600ms so the user can read the welcome script

## Loads game assets and processes (input checking interval, text)
pg.key.set_repeat(200, 100) # Sets the interval pygame checks the keyboard for new input and duration keys have to be pressed continuously to be considered held down
ExitMSG = PGUI.TextGen(50, "Thank you for playing", TEXTCOLOUR, SUBCOLOUR, WINSIZE[0] // 2, WINSIZE[1] // 2) # Centre of window
"""
MenuTitle = PGUI.TextGen(50, "Thank you for playing", TEXTCOLOUR, SUBCOLOUR, WINSIZE[0] // 2, WINSIZE[1] // 2) # Top centre of window
TutorialButton = PGUI.ImgButton(Image, X, Y)
ATestBTN = PGUI.ImgButton()
AWaveBTN = PGUI.ImgButton()
ABounceBallBTN = PGUI.ImgButton()
ATrigWaveBTN = PGUI.ImgButton()
"""

## Animation section - Loads spritesheets and assigns it to an animation class to process the spritesheet and animate it
SSTest = pg.image.load("SpriteSheets\pixil-frame-0 (2).png")
AniTest = Animation(SSTest, [32, 32], (64, 64), 10, 0.1, 10, True)
"""
SSWave = pg.image.load("SpriteSheets\SSWave.png")
AniWave = Animation(SSWave, [WINSIZE[0] // 2, WINSIZE[0] // 2], (???), 10, 0.1, 10) 
SSBounceBall = pg.image.load("SpriteSheets\SSWave.png")
AniBounceBall = Animation(SSBounceBall, [WINSIZE[0] // 2, WINSIZE[0] // 2], (???), 10, 0.1, 10) 
SSTrigWave = pg.image.load("SpriteSheets\SSWave.png")
AniTrigWave =  Animation(SSTrigWave, [WINSIZE[0] // 2, WINSIZE[0] // 2], (???), 10, 0.1, 10)
"""

## Main game
MainMenu()
MainGame()

## Exits the program
pg.Surface.fill(Window, MAINCOLOUR) # Fills the window ith a solid colour
pg.draw.rect(Window, ACCENTCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10) # Draws an empty rectangle as the window border
ExitMSG.render(Window) # Renders text object onto the window
pg.display.update() # Updates the window so that user can see changes from previous window update
pg.time.wait(700) # Pauses the program for 0.7s
pg.quit() # Exits pygame
print(f"{'':-^42}\n{' Program closed : Thank you for playing ':-^42}\n{'':-^42}") # Cursed mono line alignment