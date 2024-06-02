from graphs import *
import pytest
def test_getVectorArrowCoordinates():
    #test random vector
    assert getVectorArrowCoordinates((20,20),(30,30)) == ((50,50),(50-50*math.cos(math.pi/4+math.pi/8),50-50*math.sin(math.pi/4+math.pi/8)),(50-50*math.cos(math.pi/4-math.pi/8),50-50*math.sin(math.pi/4-math.pi/8)))
    #test null vector case
    with pytest.raises(TypeError):
        getVectorArrowCoordinates((20,300),(0,0))    
    #test pi/2 and -pi/2 angle case
    assert getVectorArrowCoordinates((20,20),(0,30)) == ((20,50),(20-50*math.cos(math.pi/2+math.pi/8),50-50*math.sin(math.pi/2+math.pi/8)),(20-50*math.cos(math.pi/2-math.pi/8),50-50*math.sin(math.pi/2-math.pi/8)))