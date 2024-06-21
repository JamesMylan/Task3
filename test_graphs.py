from graphs import *
import pytest
def test_getVectorArrowCoordinates():
    #test a vector
    assert getVectorArrowCoordinates((20,20),(30,30),50) == ((50,50),(50-50*math.cos(math.pi/4+math.pi/8),50-50*math.sin(math.pi/4+math.pi/8)),(50-50*math.cos(math.pi/4-math.pi/8),50-50*math.sin(math.pi/4-math.pi/8)))
    #test null vector case
    with pytest.raises(TypeError):
        getVectorArrowCoordinates((20,300),(0,0),50)    
    #test pi/2 and -pi/2 angle case
    assert getVectorArrowCoordinates((20,20),(0,30),50) == ((20,50),(20-50*math.cos(math.pi/2+math.pi/8),50-50*math.sin(math.pi/2+math.pi/8)),(20-50*math.cos(math.pi/2-math.pi/8),50-50*math.sin(math.pi/2-math.pi/8)))
def test_scaleVector():
    #Should be equal to 90% of the limits of the screen (225 in this case) 
    assert scaleVector((0,5000),500) == (0,225)
    assert scaleVector((0,-12304),500) == (0,-225)
    assert scaleVector((50,50),500) == (225,225)
def test_scaleVectorAddition():
    #rounded to 10 decimal places
    assert round(scaleVectorAddition(500,(0,200),(0,4000)), 10) == round(56/3, 10)
def test_getLargestCoordinateInVectors():
    assert getLargestCoordinateInVectors((23,-28),(1,0.2)) == 28
def test_drawVector():
    #Should not attempt to draw null vector
    assert drawVector("whatever","red",(0,0),(0,0)) == None