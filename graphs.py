import pygame
def drawVector(surface: pygame.Surface, color,startPos,vector,width: int = 1):
    '''
    Draws a vector line with specfied colour and width, from a specified origin
    '''
    #Pygame y coordinates increase down the screen, rather than decrease, so the y component of the vector must be subtracted
    endPos = (startPos[0]+vector[0],startPos[1]-vector[1])
    pygame.draw.line(surface, color, startPos, endPos,width)
