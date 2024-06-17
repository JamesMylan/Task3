import math
from math import radians, degrees
def addVectors(vector1:tuple,*vectors:tuple):
    """
    Adds two or more vectors and returns the resultant vector
    """
    resultantVector = vector1
    for vector in vectors:
        resultantVector = ((resultantVector[0]+vector[0]),(resultantVector[1]+vector[1]))
    return resultantVector
def subtractVectors(vector1:tuple,*vectors:tuple):
    """
    Subtracts two or more vectors and returns the resultant vector
    """
    resultantVector = vector1
    for vector in vectors:
        resultantVector = ((resultantVector[0]-vector[0]),(resultantVector[1]-vector[1]))
    return resultantVector
def toXAndY(magnitude,angle): 
    """
    Takes a vector with a given magnitude and angle (in radians) and returns it as float x and y components
    """
    #x and y components of a vector with magnitude r and angle θ can be written in the form x=rcosθ and y=rsinθ
    resultantVector = (magnitude*math.cos(angle),magnitude*math.sin(angle))
    return resultantVector 
def toAlgebraicForm(vector:tuple, nDigits: int = 10):
    """
    Takes a vector in component form and outputs algebraic form as a string
    """
    if isinstance(vector[0],float):
        xComponent = f'{round(float(vector[0]),nDigits)}i'
    else:
        xComponent = f'{int(vector[0])}i'
    if isinstance(vector[1],float):
        yComponent = f'{round(float(vector[1]),nDigits):+}j'
    else:
        yComponent = f'{int(vector[1]):+}j'
    return f'{xComponent} {yComponent}'
def getMagnitude(vector: tuple):
    """
    Calculates magnitude of a single vector
    """
    magnitude = math.sqrt((vector[0])**2+(vector[1])**2)
    return magnitude
def getVectorAngle(vector:tuple):
    #Inverse tan (math.atan) only has a range of 180°, rather than 360°. Therefore, vectors in quadrants 2 or 3 must have an angle of pi subtracted from or added to them.
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
        if vector[1] >= 0:
            vectorAngle = math.atan(vector[1]/vector[0]) +math.pi
        else:
            vectorAngle = math.atan(vector[1]/vector[0]) -math.pi
    return vectorAngle
def toMagnitudeAndAngleForm(vector: tuple):
    return getMagnitude(vector),getVectorAngle(vector)