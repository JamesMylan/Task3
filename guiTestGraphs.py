from main import *
from graphs import *
#Change function here
functionToTest = 'test_additionOfVectorsWithAxes'




# pygame setup
pygame.init()
screenWidth = 500
screenHeight = screenWidth
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True
dt = 0
origin = (screenWidth/2,screenHeight/2)
debug = False
screen.fill("white")

def test_drawVector_testArrows(surface):
    global screenWidth,ScreenHeight,origin
    vectors=[(200,123),(-200,123),(-200,-123),(200,-123)]
    for vector in vectors:
        drawVector(surface,"red",(0,0),vector)
def test_drawVector_offCentre(surface):
    global screenWidth,ScreenHeight,origin
    vectors=[(200,123),(-200,123),(-200,-123),(200,-123)]
    for vector in vectors:
        drawVector(surface,"red",(-50,-50),vector)
def test_drawAdditionOfVectors(surface):
    global screenWidth,ScreenHeight,origin
    vectors=(2,8),(13,4),(-2,1),(-4,4),(2,-14.5)
    drawAdditionOfVectors(surface,(0,0),15,*vectors)
def test_drawAxes(surface):
    global screenWidth,ScreenHeight,origin
    drawAxes(surface,(0,0))
def test_additionOfVectorsWithAxes(surface):
    global screenWidth,ScreenHeight,origin
    vectors=(2,8),(13,4),(-2,1),(-4,4),(2,-14.5)
    drawAxes(surface,(0,0),2)
    drawAdditionOfVectors(surface,(0,0),15,*vectors)
    scale = scaleVectorAddition(screenWidth,(0,0),*vectors)
    drawGridLines(surface,11,scale)



while running:
    eval(functionToTest+'(screen)')  

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
