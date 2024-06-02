import pygame, math
from main import *
def drawLine(surface: pygame.Surface, color,startPos,endPos,width: int = 1):
    """
    Draws a line with postition relative to the centre of the screen
    """
    origin=(surface.get_width()/2,surface.get_height()/2)
    #Pygame y coordinates increase down the screen, rather than decrease, so the y component of the vector must be subtracted
    pygame.draw.line(surface, color, (origin[0]+startPos[0], origin[1]-startPos[1]),(origin[0]+endPos[0], origin[1]-endPos[1]),width)
def getVectorArrowCoordinates(startPos,vector):
    """
    Given a start position and a position vector, it will calulate the cooridinates of a vector arrow on a plane
    Returns the ending coordinate of the vector, and the coordinates of the arrows of the vector
    """
    endPos=(startPos[0]+vector[0],startPos[1]+vector[1])
    #Inverse tan (math.atan) only has a range of 180°, rather than 360°. Therefore, vectors in quadrants 2 or 3 must have an angle of pi added to them.
    if vector[0] > 0:
        vectorAngle = math.atan(vector[1]/vector[0])
    elif vector[0] == 0:
        if vector[1] > 0:
            vectorAngle = math.pi/2
        elif vector[1] < 0:
            vectorAngle = -math.pi/2
        else:
            vectorAngle = None
    else: 
        vectorAngle = math.pi + math.atan(vector[1]/vector[0])
    #Get coordinates of arrows
    arrow1=(subtractVectors(endPos,toXAndY(50,vectorAngle+math.pi/8)))
    arrow2=(subtractVectors(endPos,toXAndY(50,vectorAngle-math.pi/8)))
    return endPos,arrow1,arrow2
def drawVector(surface: pygame.Surface, color,startPos,vector,width: int = 1):
    """
    Draws a vector arrow with specfied colour and width, from a specified origin
    """
    vectorArrowCoordinates = getVectorArrowCoordinates(startPos,vector)
    #Drawing vector line
    drawLine(surface, color, startPos, vectorArrowCoordinates[0],width)
    #Drawing arrowlines
    drawLine(surface,color,vectorArrowCoordinates[1],vectorArrowCoordinates[0],width)
    drawLine(surface,color,vectorArrowCoordinates[2],vectorArrowCoordinates[0],width)