# Cameron Maxwell, 251091399 , cs1026a
# Imports math function for pi
from math import pi

# Def function that determines the volume of the cube
def cubeVolume(cubeSideLength):
    cubeSideLength = float(cubeSideLength)
    volume = (cubeSideLength ** 3)
    return volume

# Def function that determines the volume of the pyramid
def pyramidVolume(pyramidBase, pyramidHeight):
    pyramidBase = float(pyramidBase)
    pyramidHeight = float(pyramidHeight)
    volume = (pyramidBase ** 2) * pyramidHeight / 1 / 3
    return volume

# Def function that determines the volume of the ellipsoid
def ellipsoidVolume(radius1, radius2, radius3):
    radius1 = float(radius1)
    radius2 = float(radius2)
    radius3 = float(radius3)
    volume = radius1 * radius2 * radius3 * (4/3 * pi)
    return volume





