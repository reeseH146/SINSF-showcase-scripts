# A series of animations the program can play which can be played
import pygame as pg
from pygame.locals import * # type: ignore
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
 - Updates the frame counter
 - Updates the image on the surface according to counter

Position update
 - Updates position depending on direction/position input
 - Updates position of surface on the display
"""
"""
 - Animation object is created with necessary parses
 - Animation.AniUpdate() called to update frame, typically every frame/loop
 - Animation.LocUpdate() called to update location, based on user input or program calculated location 
"""
class Animation:
    def __init__(self, SSheet, Loc : list, Size : tuple, Speed : float, Increment : float, SpeedChange : float, MaxFrame : int, Move = False):
        # SSheet and attributes
        self.SSheet = SSheet # Sprite sheet
        self.Loc = Loc # Location of the animation object
        self.Size = Size # Array of the size of each frame
        self.Move = Move
        # Animation attributes
        self.Speed = Speed
        self.Frame = 0
        self.Increment = Increment
        self.SpeedChange = SpeedChange
        self.MaxFrame = MaxFrame
        self.Image = pg.Surface(self.Size)
        self.rect = self.Image.get_rect()
        self.rect.center = (self.Loc[0], self.Loc[1])
        self.FrameCounter = PGUI.TextGen(40, f"{self.Frame}", TEXTCOLOUR, SUBCOLOUR, 11, 11, True, False)
        print(f"Animation object created : {self.SSheet}")

    """ Updates the animation object
    Updates frame    
    Resets frame if exceeds last frame
    Updates current frame of animation object
    """
    def AniUpdate(self):
        self.Image.blit(self.SSheet, (0, 0), (self.Size[0] * int(self.Frame), 0, self.Size[0], self.Size[1]))
        self.Frame += self.Increment # Increments frame
        if self.Frame > self.MaxFrame: # Checks if frame is above total sprites and resets if so
            self.Frame = 0
        self.FrameCounter = PGUI.TextGen(40, f"{int(self.Frame)}", TEXTCOLOUR, SUBCOLOUR, 11, 11, True, False)
        self.rect.center = (self.Loc[0], self.Loc[1])
        # Updates Window and animation frame
        self.FrameCounter.Render(Window)
        Window.blit(self.Image, self.rect)

    """ Updates position of animation object
    Checks the type of movement and whether movement is enabled
    Moves the object a set distance in a chosen direction or moves them to a specified position
    Checks the final location and resets it to touch the boundary
    """
    def LocUpdate(self, Direction = "", Position = (0, 0)):
        # Makes checks to change position of animation object
        if self.Move: # Checks movement is enabled
            if Direction == "w": # Updates vertical position
                self.Loc[1] -= self.Speed
            elif Direction == "a": # Updates horizontal position
                self.Loc[0] -= self.Speed
            elif Direction == "s": # Updates vertical position
                self.Loc[1] += self.Speed
            elif Direction == "d": # Updates horizontal position
                self.Loc[0] += self.Speed
            elif Direction == "": # Changes position if movement enabled
                self.Loc = Position
        elif Direction == "": # Changes position if movement disabled
            self.Loc = Position
        # Resets animation object position to keep it in bounds
        if self.Loc[0] <= (10 + (self.Size[0] // 2)): # If out of left x boundary
            self.Loc[0] = (10 + (self.Size[0] // 2)) # Sets position to just touch left x boundary
        elif self.Loc[0] >= ((WINSIZE[0]) - (self.Size[0] // 2)): # If out of right x boundary
            self.Loc[0] = ((WINSIZE[0] - 10) - (self.Size[0] // 2)) # Sets position to just touch right x boundary
        if self.Loc[1] <= (10 + (self.Size[1] // 2)): # If out of top y boundary
            self.Loc[1] = (10 + (self.Size[1] // 2)) # Sets position to just touch top y boundary
        elif self.Loc[1] >= ((WINSIZE[1]) - (self.Size[1] // 2)): # If out of bottom y boundary
            self.Loc[1] = ((WINSIZE[1] - 10) - (self.Size[1] // 2)) # Sets position to just touch bottom y boundary
        # Updates Window and animation in new position
        self.rect.center = (self.Loc[0], self.Loc[1])
        print(f"Location updated : {self.Loc}")

    """ Checks for user input on animation object
    Checks if mouse is within the x bound and y bound of the animation
    """
    def PosCheck(self, MPos):
        # Checks if the mouse position is within the x range and y range of character clicked
        if (self.rect[0] < MPos[0] < self.rect[0] + self.rect[2]) and (self.rect[1] < MPos[1] < self.rect[1] + self.rect[3]):
            print(f"Button clicked at {MPos}")
            return True # True if mouse pos in button range
        else:
            print(f"Button clicked at {MPos}")
            return False # False if mouse pos not in button range

    """ Updates animation speed
    Checks whether it is increasing or decreasing
    Changes by a set amount
    There is a limit to decreasing so that it can only pause and not go to negative speed
    """
    def PBSpeedUpdate(self, IncrDecr):
        if IncrDecr: # True for increasing
            self.Increment += self.SpeedChange
            print(f"Speed increased by {self.SpeedChange} to {self.Increment:.4f}")
        else: # False for decreasing
            self.Increment -= self.SpeedChange
            if self.Increment < 0:
                self.Increment = 0
            print(f"Speed decreased by {self.SpeedChange} to {self.Increment:.4f}")

# --- Main Menu ---
def MainMenu():
    # Loads the main menu visual assets and interactive assets
    Window.fill(MAINCOLOUR)
    pg.draw.rect(Window, SUBCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10)
    TestText.render(Window)
    BallText.render(Window)
    WaveText.render(Window)
    MenuTitle.Render(Window)
    pg.display.update()
    pg.event.set_allowed(K_ESCAPE)
    Running = True
    while Running:
        # Loops through the event queue checking for any events, mainly user input
        for event in pg.event.get():
            # Quits the game if user clicks on close window button (X)
            if (event.type == QUIT) or (pg.key.get_pressed()[K_ESCAPE]):
                Running = False
                pg.Surface.fill(Window, MAINCOLOUR) # Fills the window ith a solid colour
                pg.draw.rect(Window, ACCENTCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10) # Draws an empty rectangle as the window border
                ExitMSG.Render(Window) # Renders text object onto the window
                pg.display.update() # Updates the window so that user can see changes from previous window update
                pg.time.wait(700) # Pauses the program for 0.7s
                pg.quit() # Exits pygame
                print(f"{'':-^42}\n{' Program closed : Thank you for playing ':-^42}\n{'':-^42}") # Cursed mono line alignment
                quit()
            # Checks mouse button has been lifted and that it is the left mouse button
            elif (event.type == MOUSEBUTTONDOWN) and (pg.mouse.get_pressed()[0]):
                # Grabs the position of the mouse to check if it is within any buttons
                MousePosition = pg.mouse.get_pos()
                # Brings user to game which showcases the animations depending on which one they selected
                if TestText.positionCheck(MousePosition):
                    print("Rainbow animation chosen")
                    MainGame(AniTest)
                elif BallText.positionCheck(MousePosition):
                    print("Ball bounce animation chosen")
                    MainGame(AniBounceBall)
                elif WaveText.positionCheck(MousePosition):
                    print("Trig waves animation chosen")
                    MainGame(AniTrigWave)
        Clock.tick(60)

# --- Main Game ---
def MainGame(TransferedAnimation):
    ChosenAnimation = TransferedAnimation
    ChosenAnimation.LocUpdate("", [WINSIZE[0] // 2, WINSIZE[1] // 2])#, False, [32, 32])
    ## Makes some checks and updates the window to show information to the user
    pg.display.update()
    Running = True
    while Running:
        # Loops through the event queue checking for any events, mainly user input
        for event in pg.event.get():
            # Grabs a list of the state of all possible events
            Events = pg.key.get_pressed()
            # Quits the game if user clicks on close window button (X)
            if event.type == QUIT:
                Running = False
                pg.Surface.fill(Window, MAINCOLOUR) # Fills the window ith a solid colour
                pg.draw.rect(Window, ACCENTCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10) # Draws an empty rectangle as the window border
                ExitMSG.Render(Window) # Renders text object onto the window
                pg.display.update() # Updates the window so that user can see changes from previous window update
                pg.time.wait(700) # Pauses the program for 0.7s
                pg.quit() # Exits pygame
                print(f"{'':-^42}\n{' Program closed : Thank you for playing ':-^42}\n{'':-^42}") # Cursed mono line alignment
                quit()
            elif Events[K_ESCAPE]: # Returns back to main menu
                pg.event.set_blocked(K_ESCAPE)
                MainMenu()
            elif Events[K_TAB]: # Brings animation object to the center of the screen
                ChosenAnimation.LocUpdate("", [WINSIZE[0] // 2, WINSIZE[1] // 2])#, False, [32, 32])
            # Changes position of the animation object based on direction
            if ChosenAnimation.Move:
                if Events[K_w]:
                    ChosenAnimation.LocUpdate("w")
                    print("Moved up")
                if Events[K_a]:
                    ChosenAnimation.LocUpdate("a")
                    print("Moved left")
                if Events[K_s]:
                    ChosenAnimation.LocUpdate("s")
                    print("Moved down")
                if Events[K_d]:
                    ChosenAnimation.LocUpdate("d")
                    print("Moved right")
            # Changes the speed which the animation plays at
            if Events[K_LEFT]:
                ChosenAnimation.PBSpeedUpdate(False) # Decreases animation playback speed
            elif Events[K_RIGHT]:
                ChosenAnimation.PBSpeedUpdate(True) # Increases animation playback speed
        # Updates the sprite
        Window.fill(MAINCOLOUR)
        pg.draw.rect(Window, SUBCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10)
        ChosenAnimation.AniUpdate()
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
Icon = pg.image.load(r"Animation demonstration\SpriteSheets\KES.png") # type: ignore # Loads image used for program icon
WellcomeMsg = PGUI.TextGen(50, "Welcome to the animation demonstration", TEXTCOLOUR, SUBCOLOUR, WINSIZE[0] // 2, WINSIZE[1] // 2) # Centre of window
pg.display.set_icon(Icon) # Sets loaded image of KES to window icon
pg.display.set_caption("Animation Demonstration") # Sets window caption of what this program is to the user
Window = pg.display.set_mode(WINSIZE) # Creates the window
pg.Surface.fill(Window, MAINCOLOUR) # Fills window with a background colour
pg.draw.rect(Window, ACCENTCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10) # Draws an empty rectangle as the window border
WellcomeMsg.Render(Window) # Places a welcome message onto the window for the user
pg.display.update() # Updates the differences in the window since last update/creation so user can see changes
pg.time.wait(600) # Waits 600ms so the user can read the welcome script

## Animation section - Loads sprite sheets and assigns it to an animation class to process the sprite sheet and animate it
SSTest = pg.image.load(r"Animation demonstration\SpriteSheets\Rainbow.png")
SSBall = pg.image.load(r"Animation demonstration\SpriteSheets\BounceBall.png").convert_alpha()
SSWave = pg.image.load(r"Animation demonstration\SpriteSheets\TrigGraphs.png").convert_alpha()
AniLoc = [int(WINSIZE[0] // 2), int(WINSIZE[1] // 2)]
### Test Animation values and stuff
# TODO : AniTest Animation Values
AniTestSpeed = 15 # D15 - The distance the animation object can travel
AniTestIncrement = 0.1 # D0.1 - Rate of change of animation frames
AniTestSpeedChange = 0.01 #D0.01 - Step in change of Increment
AniTest = Animation(SSTest, AniLoc, (64, 64), AniTestSpeed, 0.1, AniTestSpeedChange, 10, True)
# TODO : BounceBall Animation Values
AniBallSpeed = 15 # D15 - The distance the animation object can travel
AniBallIncrement = 0.1 # D0.1 - Rate of change of animation frames
AniBallSpeedChange = 0.01 #D0.01 - Step in change of Increment
AniBounceBall = Animation(SSBall, AniLoc, (100, 250), AniBallSpeed, 0.1, AniBallSpeedChange, 30, True) 
# TODO : TrigWaves Animation Values
AniWaveSpeed = 15 # D15 - The distance the animation object can travel
AniWaveIncrement = 0.0000000000001 # D0.1 - Rate of change of animation frames
AniWaveSpeedChange = 0.1 #D0.01 - Step in change of Increment
AniTrigWave =  Animation(SSWave, AniLoc, (540, 540), AniWaveSpeed, 0.1, AniWaveSpeedChange, 106)

## Loads game assets and processes (input checking interval, text)
pg.key.set_repeat(200, 1000) # Sets the interval pygame checks the keyboard for new input and duration keys have to be pressed continuously to be considered held down
ExitMSG = PGUI.TextGen(50, "Thank you for playing", TEXTCOLOUR, SUBCOLOUR, WINSIZE[0] // 2, WINSIZE[1] // 2) # Centre of window
MenuTitle = PGUI.TextGen(40, "Please select an animation", TEXTCOLOUR, SUBCOLOUR, WINSIZE[0] // 2, 35) # Top centre of window
TestText = PGUI.TextButton(50, "Rainbow square Animation", True, [SUBCOLOUR, TEXTCOLOUR], WINSIZE[0] // 2, WINSIZE[1] * (3/6) - 100) # Top of 3 in centre
BallText = PGUI.TextButton(50, "Bouncing ball Animation", True, [SUBCOLOUR, TEXTCOLOUR], WINSIZE[0] // 2, WINSIZE[1] * (4/6) - 100) # Middle of 3 in centre
WaveText = PGUI.TextButton(50, "Trig wave Animation", True, [SUBCOLOUR, TEXTCOLOUR], WINSIZE[0] // 2, WINSIZE[1] * (5/6) - 100) # Bottom of 3 in centre


## Main game
MainMenu()
# Exits the program
pg.Surface.fill(Window, MAINCOLOUR) # Fills the window ith a solid colour
pg.draw.rect(Window, ACCENTCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10) # Draws an empty rectangle as the window border
ExitMSG.Render(Window) # Renders text object onto the window
pg.display.update() # Updates the window so that user can see changes from previous window update
pg.time.wait(700) # Pauses the program for 0.7s
pg.quit() # Exits pygame
print(f"{'':-^42}\n{' Program closed : Thank you for playing ':-^42}\n{'':-^42}") # Cursed mono line alignment

# TODO : Rename animation class variables
# TODO : Fix animation spritesheets
# TODO : Edit comments