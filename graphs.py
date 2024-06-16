import pygame, math
from main import *
def drawLine(surface: pygame.Surface, color,startPos,endPos,width: int = 1):
    """
    Draws a line with postition relative to the centre of the screen
    """
    origin=(surface.get_width()/2,surface.get_height()/2)
    #Pygame y coordinates increase down the screen, rather than decrease, so the y component of the vector must be subtracted
    pygame.draw.line(surface, color, (origin[0]+startPos[0], origin[1]-startPos[1]),(origin[0]+endPos[0], origin[1]-endPos[1]),width)
def scaleVector(vector,screenWidth):
    """
    Scales a vector to fit within 90% of the screenWidth
    Returns shrunken or enlarged vector tuple
    """
    #Get the abosulute value of each coordinate
    positiveVector = tuple(abs(x) for x in vector)
    scale = max(positiveVector)/(0.9*screenWidth/2)
    resultantVector = tuple(x/scale for x in vector)
    #Returns shrunken or enlarged vector
    return resultantVector
def getLargestCoordinateInVectors(*vectors: tuple):
    """
    Returns the absolute value of the largest coordinate by magnitude
    """
    absoluteVectors = []
    for vector in vectors:
        for coordinate in vector:
            absoluteVectors.append(abs(coordinate))
    return max(absoluteVectors)
def getVectorArrowCoordinates(startPos,vector,arrowLength: float = -1):
    """
    Given a start position and a position vector, it will calulate the cooridinates of a vector arrow on a plane
    Returns the ending coordinate of the vector, and the coordinates of the arrows of the vector
    """
    if arrowLength == -1:
        arrowLength = getMagnitude(vector)/8
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
    arrow1=(subtractVectors(endPos,toXAndY(arrowLength,vectorAngle+math.pi/8)))
    arrow2=(subtractVectors(endPos,toXAndY(arrowLength,vectorAngle-math.pi/8)))
    return endPos,arrow1,arrow2
def drawVector(surface: pygame.Surface, color,startPos,vector,arrowLength: float = -1,width: int = 1):
    """
    Draws a vector arrow with specfied colour and width, from a specified origin
    """
    if vector == (0,0):
        return None
    vectorArrowCoordinates = getVectorArrowCoordinates(startPos,vector,arrowLength)
    #Drawing vector line
    drawLine(surface, color, startPos, vectorArrowCoordinates[0],width)
    #Drawing arrowlines
    drawLine(surface,color,vectorArrowCoordinates[1],vectorArrowCoordinates[0],width)
    drawLine(surface,color,vectorArrowCoordinates[2],vectorArrowCoordinates[0],width)
def scaleVectorAddition(screenWidth,startPos,*vectors):
    """
    Calculates the scale factor needed to fit the addition of multiple vectors inside of screenWidth
    Returns scale factor to apply to all vectors
    """
    endPoses = []
    for vector in vectors:
        endPos = getVectorArrowCoordinates(startPos,vector)[0]
        endPoses.append(endPos)
        startPos = endPos
    largestCoordinate = getLargestCoordinateInVectors(*endPoses)
    scale = largestCoordinate/(0.9*screenWidth/2)
    return scale    
def drawAdditionOfVectors(surface: pygame.Surface, startPos, arrowLength: float = -1, *vectors):
    scale = scaleVectorAddition(surface.get_width(),startPos,*vectors)
    nextStartPos = startPos
    colours = ["red","blue","green","purple","brown","orange","plum","aqua","burlywood","gold"]
    for index, vector in enumerate(vectors):
        vector = tuple(x/scale for x in vector)
        endPos = getVectorArrowCoordinates(nextStartPos,vector)[0]
        drawVector(surface,colours[index % len(colours)],nextStartPos,vector,arrowLength)
        nextStartPos = endPos
    resultantVector = addVectors(*vectors)
    drawVector(surface,"black",startPos,tuple(x/scale for x in resultantVector))
def drawAxes(surface: pygame.Surface, position, width: int = 1):
    drawLine(surface,"gray",(position[0],0),(position[0],surface.get_width()/2),width)
    drawLine(surface,"gray",(position[0],0),(position[0],-surface.get_width()/2),width)
    drawLine(surface,"gray",(0,position[1]),(surface.get_width()/2,position[1]),width)
    drawLine(surface,"gray",(0,position[1]),(-surface.get_width()/2,position[1]),width)
    