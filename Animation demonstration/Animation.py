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
    def __init__(self, SSheet, Loc : [], Size : (), Speed : int, Increment : float, MaxFrame : int):
        # SSheet and attributes
        self.SSheet = SSheet
        self.Loc = Loc
        self.Size = Size
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



# --- Main Menu ---
def MainMenu():
    Window.fill(MAINCOLOUR)
    pg.draw.rect(Window, SUBCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10)

    # Create assets and load them here

    Running = True
    while Running:
        # Loops through the event queue checking for any events, mainly user input
        for event in pg.event.get():
            # Grabs a list of the state of all possible events
            Events = pg.event.get()
            # Quits the game if user clicks on close window button (X)
            if event.type == QUIT:
                Running = False
                pg.quit()
                print(f"{'':-^42}\n{' Program closed : Thank you for playing ':-^42}\n{'':-^42}") # Cursed mono line alignment
                quit()
            if Events[MOUSEBUTTONDOWN]:
                MouseLocation = pg.mouse.get_pos()

                # Checks mouse location in boxes

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
                pass

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
print(f"{'':-^42}\n{' Program loaded : Please enjoy playing ':-^42}\n{'':-^42}") # Cursed mono line alignment

## Default values
WINSIZE = (1920 * 0.65, 1080 * 0.65)
Clock = pg.time.Clock()
MAINCOLOUR = (255, 191, 70)
SUBCOLOUR = (87, 87, 91)
ACCENTCOLOUR = (147, 147, 158)
TEXTCOLOUR = (255, 255, 255)

pg.key.set_repeat(200, 100)

## Animation section
"""
Sprite sheet is loaded
Counter for current frame is made
Step for counter is made
Size of the image is made

Size of the image and current frame is used to calculate section of sprite sheet to load later
"""
SpriteSheet = pg.image.load("pixil-frame-0 (2).png")
Ani1 = Animation(SpriteSheet, [32, 32], (64, 64), 10, 0.1, 10)

## Loads assets used in the game
WellcomeMsg = PGUI.TextGen(50, "Welcome to the animation demonstration", TEXTCOLOUR, SUBCOLOUR, WINSIZE[0] // 2, WINSIZE[1] // 2)


## Loads the window and welcomes the user
pg.display.set_caption("Animation Demonstration")
Window = pg.display.set_mode(WINSIZE)
pg.Surface.fill(Window, MAINCOLOUR)
pg.draw.rect(Window, ACCENTCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10)
WellcomeMsg.render(Window)
pg.display.update()
pg.time.wait(1500)

## Main game
MainMenu()
MainGame()

pg.quit()
print(f"{'':-^42}\n{' Program closed : Thank you for playing ':-^42}\n{'':-^42}") # Cursed mono line alignment