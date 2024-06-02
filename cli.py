from main import *
from graphs import *
import pygame
vectors=[]
numberOfVectors=input("Number of vectors to add: ")
for i in range(int(numberOfVectors)):
    vectors.append(tuple(float(x) for x in input("Enter vector separted by spaces: ").split()))
resultantVector = addVectors(*vectors)
#Null vector is special case
if resultantVector == (0,0):
    print("Result is the zero vector")
else:
    print("Resultant vector is "+toAlgebraicForm(resultantVector))
    if input("Would you like to view the graphical representation? Y/N: ") == "Y":
        # pygame setup
        pygame.init()
        screenWidth = 500
        screenHeight = screenWidth
        screen = pygame.display.set_mode((screenWidth, screenHeight))
        clock = pygame.time.Clock()
        running = True
        dt = 0
        while running:
            screen.fill("white")
            drawAdditionOfVectors(screen,-1,*vectors)
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            #Limits FPS
            dt = clock.tick(15) / 1000
