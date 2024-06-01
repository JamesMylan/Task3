from main import *
from graphs import *
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
debug = False
screen.fill("white")

def test_drawVector(surface):
    global screenWidth,ScreenHeight,origin
    vectors=[(200,123),(-200,123),(-200,-123),(200,-123)]
    for vector in vectors:
        drawVector(surface,"red",(0,0),vector)

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
