from graphs import *
import pygame
#Change function here
functionToTest = 'drawVector'

# pygame setup
pygame.init()
screenWidth = 500
ScreenHeight = 500
screen = pygame.display.set_mode((screenWidth, ScreenHeight))
clock = pygame.time.Clock()
running = True
dt = 0
origin = (screenWidth/2,ScreenHeight/2)
debug = True
screen.fill("white")

def test_drawVector(surface):
    global screenWidth,ScreenHeight,origin
    vector=(-200,123)
    drawVector(surface,"red",origin,vector)

while running:
    eval('test_'+functionToTest+'(screen)')  

    if debug:
        print(pygame.mouse.get_pos())

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    #Limits FPS
    dt = clock.tick(5) / 1000

pygame.quit()
