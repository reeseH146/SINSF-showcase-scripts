# A series of animations the program can play which can be played
import pygame as pg
from pygame.locals import *
pg.init()
import PGUI

# --- Main Menu ---
def MainMenu():
    Window.fill(MAINCOLOUR)
    pg.draw.rect(Window, SUBCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10)
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
        pg.display.update()
        Clock.tick(60)

# --- Main Game ---
def MainGame():
    Window.fill(MAINCOLOUR)
    pg.draw.rect(Window, SUBCOLOUR, (0, 0, WINSIZE[0], WINSIZE[1]), 10)
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
DefAniSpeed = []
DefAniScale = 1
DefAniPos = [0, 0]
Animations = []

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