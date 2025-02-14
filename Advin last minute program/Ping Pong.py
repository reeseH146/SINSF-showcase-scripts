import pygame as pg
from random import randint as rint

# Ball class
class Ball:
    def __init__(self, Loc, Speed, Size):
        self.Ball = pg.transform.scale(pg.image.load(r"Advin last minute program/Ball.png"), (100, 100))
        self.HitBox = self.Ball.get_rect()
        self.Loc = Loc
        self.Speed = Speed
        self.Size = Size
        self.Colour = (255, 0, 0)
        self.Direction = [1, 1]
        
    def Display(self, Window):
        Window.blit(self.Ball, (int(self.Loc[0]), int(self.Loc[1])))
    
    def Move(self):
        # Moves left
        if self.Direction[0] == 0:
            self.Loc[0] -= self.Speed
        # Moves right
        elif self.Direction[0] == 1:
            self.Loc[0] += self.Speed
        
            
    def Collision(self, P1, P2):
        if self.HitBox.colliderect(P1):
            self.Direction[0] = 1
        if self.HitBox.colliderect(P2):
            self.Direction[1] = 0
            
    
# Paddle class
class Paddle:
    def __init__(self, Loc, Speed, Size):
        self.Loc = Loc
        self.Speed = Speed
        self.Size = Size
        self.Rect = pg.Rect(self.Loc, self.Size)
        self.Colour = (255, 255, 255)
        
    # Updates the rect onto the window
    def Display(self, Window):
        pg.draw.rect(Window, self.Colour, self.Rect)
    
    # Updates the position of the paddle
    def Move(self, Direction):
        # Move up
        if Direction == 1:
            self.Rect.y -= self.Speed
            # Rests paddle position if leaves border
            if self.Rect.y < 0:
                self.Rect.y = 0
        # Rests paddle position if leaves border
        elif Direction == -1:
            self.Rect.y += self.Speed
            if self.Rect.y + self.Size[1] > WinSize[1]:
                self.Rect.y = WinSize[1] - self.Size[1]
    
# Main
# Initialise
WinSize = [1200, 675]
BGCOLOUR = (125, 255, 160) # Mint Green
Display = pg.display.set_mode(WinSize)
pg.display.set_caption("Ping Pong")

# Set up window
Display.fill(BGCOLOUR)
P1Paddle = Paddle([10, WinSize[1]//2 - 100], 1, [15, 200])
P1Paddle.Display(Display)
P2Paddle = Paddle([1175, WinSize[1]//2 - 100], 1, [15, 200])
P2Paddle.Display(Display)
BallObj = Ball([WinSize[0]//2, WinSize[1]//2], 0.85, 15)
BallObj.Display(Display)
pg.display.update()
# Main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    Keys = pg.key.get_pressed()
    if Keys[pg.K_ESCAPE]:
        pg.quit()
        quit()
    # Paddle left movement
    if Keys[pg.K_w]: # Move up
        P1Paddle.Move(1)
    elif Keys[pg.K_s]: # Move down
        P1Paddle.Move(-1)
    # Paddle right movement
    if Keys[pg.K_UP]: # Move up
        P2Paddle.Move(1)
    elif Keys[pg.K_DOWN]: # Move down
        P2Paddle.Move(-1)
        
    BallObj.Move()
    
    Display.fill(BGCOLOUR)
    P1Paddle.Display(Display)
    P2Paddle.Display(Display)
    BallObj.Display(Display)
    pg.display.update()