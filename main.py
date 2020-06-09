# Author: Cameron Maxwell
# This program calculates the volume of different shapes, sorts them into lists, and saves them into files.

# Imports the cube, pyramid, and ellipsoid volume from the Volume
from volumes import cubeVolume, pyramidVolume, ellipsoidVolume
# Imports the summarize function
import summarize

# Integer variables for the shapes
cubeSideLength = 0
pyramidBase = 0
pyramidHeight = 0
radius1 = 0
radius2 = 0
radius3 = 0
# Lists that contain strings that the user input must match
quitList = ["quit", "q"]
cubeList = ["cube", "c"]
pyramidList = ["pyramid", "p"]
ellipsoidList = ["ellipsoid", "e"]
# Empty lists that will later store volumes of the shapes
clist = []
plist = []
elist = []


# Def function formats the user input
def formatInput(textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine


# Asks user to input a test case number
print("Type cube or c, pyramid or p, ellipsoid or e, to select shape. Type quit or q to stop program. Enter test case number to organize multiple outputs. ")
testNumber = int(input("Enter test case number:"))

# Sets the string variable for the inputted shape
shapeSelection = ""
# While loop asks user to enter a shape and will continue looping until user inputs a string in the quitList
while shapeSelection not in quitList:
    shapeSelection = input("Enter shape:")
    # Formats input
    shapeSelection = formatInput(shapeSelection)
    # If statement checks to see if the input is in the cubeList
    if shapeSelection in cubeList:
        # Asks user for length of side
        cubeSideLength = input("Enter length of side:")
        # If statement checks to see if the length is a digit and also allows decimal numbers
        if cubeSideLength.replace(".", "", 1).isdigit():
            # Adds the cube volume to the cube volume list and rounds off decimals to the nearest hundredth
            clist.append(float("%.3f" % cubeVolume(cubeSideLength)))
            # Sorts the volumes in the list from lowest to highest
            clist = sorted(clist)
            # Prints the volume of the cube that was just entered by the user
            print("Cube Volume:", ("%.3f" % cubeVolume(cubeSideLength)))
        # If the inputted side length is not a number, string message will be printed
        else:
            print("Not a number!")
    # Elif statement checks to see if the inputted shape is in the pyramidList
    elif shapeSelection in pyramidList:
        # Asks user for length of base
        pyramidBase = input("Enter length of base:")
        # Asks user for length of height
        pyramidHeight = input("Enter length of height:")
        # If statement checks to see that both inputs are numbers and will also allow decimals
        if pyramidBase.replace(".", "", 1).isdigit() and pyramidHeight.replace(".", "", 1).isdigit():
            # Adds the pyramid volume to the pyramid volume list and rounds off decimals to the nearest hundredth
            plist.append(float("%.3f" % pyramidVolume(pyramidBase, pyramidHeight)))
            # Sorts the pyramid volume list from lowest to highest
            plist = sorted(plist)
            # Prints the volume of the pyramid that was just entered by the user
            print("Pyramid Volume:", ("%.3f" % pyramidVolume(pyramidBase, pyramidHeight)))
        # If the inputted side length is not a number, string message will be printed
        else:
            print("Not valid numbers!")
    # Elif statement checks to see if the inputted shape is in the ellipsoidList
    elif shapeSelection in ellipsoidList:
        # Asks user to input the 3 radiuses
        radius1 = input("Enter length of radius 1:")
        radius2 = input("Enter length of radius 2:")
        radius3 = input("Enter length of radius 3:")
        # If statement checks to see if all of the inputs are numbers and will also accept decimals
        if radius1.isnumeric() and radius2.isnumeric() and radius3.isnumeric():
            # Adds the ellipsoid volume to the ellipsoid volume list and rounds off decimals to the nearest hundredth
            elist.append(float("%.3f" % ellipsoidVolume(radius1, radius2, radius3)))
            # Sorts the volumes in the list from lowest to greatest
            elist = sorted(elist)
            # Prints the volume of the ellipsoid that was just entered by the user
            print("Ellipsoid Volume:", ("%.3f" % ellipsoidVolume(radius1, radius2, radius3)))
        # If the inputted side length is not a number, string message will be printed
        else:
            print("Not valid numbers!")
    # If the inputted shape is not a valid shape, string message will be printed
    else:
        if shapeSelection not in quitList:
            print("Not a valid shape!")
# If user enters an input in the quitList, program will display all of the volume lists
if shapeSelection in quitList:
    print("You have reached the end of the session!\nThe volumes calculated for each shape are:")
    # If all of the lists are empty, program will say no volume calculations
    if len(clist) == 0 and len(plist) == 0 and len(elist) == 0:
        print("You did not perform any volume calculations.")

    # If the cube list is empty, string message will be outputted saying no cubes entered
    if len(clist) == 0:
        print("Cube: No shapes entered.")
    # If there are volumes in the cube list, the list will be printed out
    else:
        print("Cube:", clist)
    # If the pyramid list is empty, string message will be outputted saying no pyramids entered
    if len(plist) == 0:
        print("Pyramid: No shapes entered.")
    # If there are volumes in the cube list, the list will be printed out
    else:
        print("Pyramid:", plist)
    # If the ellipsoid list is empty, string message will be outputted saying no ellipsoids entered
    if len(elist) == 0:
        print("Ellipsoid: No shapes entered.")
    # If there are volumes in the cube list, the list will be printed out
    else:
        print("Ellipsoid:", elist)
# Calls the summarize function
summarize.summarize(clist, plist, elist, testNumber)
