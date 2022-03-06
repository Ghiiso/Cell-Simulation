import pygame
def init():
    global displaySettings,resolution,MainWindow
    displaySettings = pygame.display.Info()
    resolution = (displaySettings.current_w-100,displaySettings.current_h-100)
    MainWindow = pygame.display.set_mode(resolution,0)

    global red,green,blue,white,black,speed0,varSpeed,g,tickSpeed,RadtoDeg,fps
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    white = (255,255,255)
    black = (0,0,0)
    speed0 = 5
    varSpeed = 0
    g = 1
    tickSpeed = 0.02
    RadtoDeg = 360/(3.14*2)
    fps = 60