from main import *
def test_addVectors():
    #basic addition
    assert addVectors((2,3),(7,4)) == (9,7)
    assert addVectors((3.23423,1.83),(2.0,2)) == (5.23423,3.83)
    #check floating point error to 15 decimal places
    assert tuple(round(x,10) for x in addVectors((1.47,0),(2,0))) == (3.47,0)
    #add multiple vectors
    assert addVectors((1,2),(2,30),(-12,13)) == (-9,45)
def test_subtractVectors():
    assert tuple(round(x,10) for x in subtractVectors((6.14,7.18),(13.14,30.5))) == (-7,-23.32)
def test_toXAndY():
    assert toXAndY(3,radians(20)) == (3*math.cos(radians(20)),3*math.sin(radians(20)))
    assert toXAndY(6.11,radians(32.11)) == (6.11*math.cos(radians(32.11)),6.11*math.sin(radians(32.11)))
def test_toAlgebraicForm():
    assert toAlgebraicForm((5,-6)) == "5i -6j"
    assert toAlgebraicForm((5.2,2.77723)) == "5.2i +2.77723j"
def test_intermodules():
    assert toAlgebraicForm(addVectors((2,-3),(-0.2212738,1),(2,1.1))) == "3.7787262i -0.9j"
def test_getMagnitude():
    assert getMagnitude((50,50)) == 50*math.sqrt(2)
    assert getMagnitude((0,100)) == 100

