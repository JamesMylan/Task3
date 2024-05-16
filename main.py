def addVectors(vector1:tuple,*args):
    resultantVector = vector1
    for vector in args:
        resultantVector = ((resultantVector[0]+vector[0]),(resultantVector[1]+vector[1]))
    return resultantVector

