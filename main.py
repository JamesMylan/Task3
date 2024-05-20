import math
from math import radians
def addVectors(vector1:tuple,*vectors:tuple):
    """
    Adds two or more vectors and returns the resultant vector
    """
    resultantVector = vector1
    for vector in vectors:
        resultantVector = ((resultantVector[0]+vector[0]),(resultantVector[1]+vector[1]))
    return resultantVector
def toXAndY(magnitude,angle): 
    """
    Takes a vector in magnitude-angle form and returns it as float x and y components
    """
    resultantVector = (magnitude*math.cos(radians(angle)),magnitude*math.sin(radians(angle)))
    return resultantVector
def toAlgebraicForm(vector:tuple):
    """
    Takes a vector in component form and outputs algebraic form as a string
    """
    if isinstance(vector[0],float):
        xComponent = f'{float(vector[0])}i'
    else:
        xComponent = f'{int(vector[0])}i'
    if isinstance(vector[1],float):
        yComponent = f'{float(vector[1]):+}j'
    else:
        yComponent = f'{int(vector[1]):+}j'
    return f'{xComponent} {yComponent}'