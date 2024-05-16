from main import *
def test_addVectors():
    assert addVectors((2,3),(7,4)) == (9,7)
    assert addVectors((3.23423,1.83),(2.0,2)) == (5.23423,3.83)
    #add multiple vectors
    assert addVectors((1,2),(2,30),(-12,13)) == (-9,45)
def test_toXAndY():
    assert toXAndY(3,20) == (3*math.cos(radians(20)),3*math.sin(radians(20)))

