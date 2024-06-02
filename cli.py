from main import *
from graphs import *
import pygame
vectors=[]
numberOfVectors=input("Number of vectors to add: ")
for i in range(int(numberOfVectors)):
    vectors.append(tuple(float(x) for x in input("Enter vector separted by spaces: ").split()))
    print(vectors)
resultantVector = addVectors(*vectors)
if resultantVector == (0,0):
    print("Result is the zero vector")
else:
    print("Resultant vector is "+toAlgebraicForm(resultantVector))
    if input("Would you like to view the graphical representation? Y/N: ") == "Y":
        # pygame setup
        pygame.init()
        screenWidth = 500
        ScreenHeight = 500
        screen = pygame.display.set_mode((screenWidth, ScreenHeight))
        clock = pygame.time.Clock()
        running = True
        dt = 0
        while running:
            screen.fill("white")
            scale = scaleVectorAddition(500,*vectors)
            startPos = (0,0)
            for vector in vectors:
                vector = tuple(x/scale for x in vector)
                endPos = getVectorArrowCoordinates(startPos,vector)[0]
                drawVector(screen,"red",startPos,vector)
                startPos = endPos
            drawVector(screen,"black",(0,0),tuple(x/scale for x in resultantVector))
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            #Limits FPS
            dt = clock.tick(15) / 1000
