import pygame, math
from main import *
def drawLine(surface: pygame.Surface, color,startPos,endPos,width: int = 1):
    '''
    Draws a line with postition relative to the centre of the screen
    '''
    origin=(surface.get_width()/2,surface.get_height()/2)
    #Pygame y coordinates increase down the screen, rather than decrease, so the y component of the vector must be subtracted
    pygame.draw.line(surface, color, (origin[0]+startPos[0], origin[1]-startPos[1]),(origin[0]+endPos[0], origin[1]-endPos[1]),width)
def drawVector(surface: pygame.Surface, color,startPos,vector,width: int = 1):
    '''
    Draws a vector arrow with specfied colour and width, from a specified origin
    '''
    #Drawing vector line
    endPos=(startPos[0]+vector[0],startPos[1]+vector[1])
    drawLine(surface, color, startPos, endPos,width)
    #Drawing arrowlines
    #Inverse tan (math.atan) only has a range of 180°, rather than 360°. Therefore, vectors in quadrants 2 or 3 must have an angle of pi added to them.
    if vector[0] > 0:
        vectorAngle = math.atan(vector[1]/vector[0])
    else:
        vectorAngle = math.pi + math.atan(vector[1]/vector[0])
    #Get coordinates of arrows
    arrow1=(subtractVectors(endPos,toXAndY(50,vectorAngle+math.pi/8)))
    arrow2=(subtractVectors(endPos,toXAndY(50,vectorAngle-math.pi/8)))
    #Draw arrows
    drawLine(surface,color,arrow1,endPos,width)
    drawLine(surface,color,arrow2,endPos,width)