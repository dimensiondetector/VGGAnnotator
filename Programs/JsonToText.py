#Author: Dimension Detector Team
#Program that converts JSON file into a series of text files
#Text file format: OBJECT_# X_WIDTH_RATIO Y_HEIGHT_RATIO OBJECT_WIDTH_RATIO OBJECT_HEIGHT_RATIO
#Uses image width and height from ImageSizes folder in project main

#IMPORT STATEMENTS
import json
from PIL import Image

#OBJECT DICTIONARY DECLARATIONS
objects = {
    'car': 1,
    'truck': 2,
    'semi': 3,
    'streetsign': 4, #ex.stop sign
    'trafficlight': 5, #red,yellow,green
    'streetlight': 6,
    'firehydrant': 7,
    'person': 8,
    'door': 9,
    'window': 10,
    'building': 11

}

#Read JSON File and break down json_data
with open('test.json') as json_data:
    jsonfile = json.load(json_data)

    #In JSON, each image is broken down into an array; Read each image array
    for image in jsonfile:
        #Assign the current image to a variable
        currentImage = jsonfile[image]

        #Retreive image name and replace extensions with .txt
        imagename = currentImage['filename']
        nameString = currentImage['filename']
        nameString = nameString.replace(".jpg", ".txt")
        nameString = nameString.replace(".Jpg", ".txt")
        nameString = nameString.replace(".JPG", ".txt")
        nameString = nameString.replace(".jpeg", ".txt")
        nameString = nameString.replace(".Jpeg", ".txt")
        nameString = nameString.replace(".JPEG", ".txt")
        nameString = nameString.replace(".png", ".txt")
        nameString = nameString.replace(".Png", ".txt")
        nameString = nameString.replace(".PNG", ".txt")
        nameString = nameString.replace(".gif", ".txt")
        nameString = nameString.replace(".Gif", ".txt")
        nameString = nameString.replace(".GIF", ".txt")

        #=================================================
        #            READ IMAGE WIDTH AND HEIGHT
        #=================================================

        #Path to find image
        path = ('C:/Users/SHEETHAL/Documents/GitHub/Annotator/VGGAnnotator/Images/' + imagename)
        #Open image at path
        img = Image.open(path)
        pixel = img.size
        #Assign width and height to variables
        width = float(pixel[0])
        height = float(pixel[1])

        # OLD code to read image width and height from ImageSizes folder
        '''
        #Identify path to retrieve the full images height and width
        path = ('C:/Users/SHEETHAL/Documents/GitHub/Annotator/VGGAnnotator/ImageSizes/' + nameString)
        #Open text file at path with read-only; Read first number as width & second number as height
        textfile = open(path, "r")
        lines = textfile.read().split(' ')
        width = float(lines[0])
        height = float(lines[1])
        #Finish reading the full image dimension text file
        textfile.close()
        '''
        #Create object text file with write capabilities into the TextFiles folder in project main
        f = open('C:/Users/SHEETHAL/Documents/GitHub/Annotator/VGGAnnotator/TextFiles/' + nameString, 'w')
        count = 0
        #=================================================
        #            READ OBJECT SQUARES LOOP
        #=================================================

        #Boolean to tell if first value in text file; Used for printing to next line sequentially
        firstLine = True

        #Obtain each object square drawn in the specific picture
        for square in currentImage['regions']:
            specificSquare = currentImage['regions'][square]

            #Retrieve the object name attached to the drawn square
            objectName = specificSquare['region_attributes']['object']

            #Lowercase the object name for comparison with the dictionary
            objectName.lower()

            #If object name is not valid, print an error statement.
            #WARNING: THIS DOES NOT STOP THE FILE FROM BEING CREATED.
            #IF A WARNING APPEARS ON CONSOLE WHEN RUNNING, PLEASE ENSURE THAT
            #CREATED FILE IS FIXED OR DELETED OR IT WILL CAUSE ISSUES WITH YOLO
            if objectName not in objects:
                print("\nError in: " + imagename)
                print("Did not create file: " + nameString)
                print("Object name - " + objectName + " - does not match a known object.\n")
            else:
                #Object exists in dictionary; if first line in file, do not print on new line
                #Subsequent lines will print a new line.
                if (firstLine == True):
                    #If object shape is not a rectangle throw an error; else continue
                    if specificSquare['shape_attributes']['name'] != "rect":
                        print("Error in file: " + nameString)
                        print("Object: " + objectName + " does not follow rectangle format.")
                    else:
                        f.write(str(objects[objectName]))
                        firstLine = False
                        #Print statement to alert user that filename is correct and added to file.
                        count = count + 1
                else:
                    #If object shape is not a rectangle throw an error; else continue
                    if specificSquare['shape_attributes']['name'] != "rect":
                        print("Error in file: " + nameString)
                        print("Object: " + objectName + " does not follow rectangle format.")
                    else:
                        f.write("\n" + str(objects[objectName]))
                        #Print statement to alert user that filename is correct and added to file.
                        count = count + 1

                #=================================================
                #            READ SQUARE ATTRIBUTES LOOP
                #=================================================

                #Obtain square-object x y width and height attributes
                for objectDetails in specificSquare['shape_attributes']:
                    objectDimensions = specificSquare['shape_attributes'][objectDetails]
                    #Do not obtain rectangle parameter
                    if (objectDimensions != "rect" and objectDimensions != "circle" and objectDimensions != "ellipse" and objectDimensions != "polygon" and objectDimensions != "point"):
                        if (objectDimensions == "x" or objectDimensions == "width"):
                            objectDimensions = float(objectDimensions / width)
                            f.write(" " + str(objectDimensions))
                        else:
                            objectDimensions = float(objectDimensions / height)
                            f.write(" " + str(objectDimensions))

        # Print new line to seperate image print outs on console.
        print("\n" + nameString + " has " + str(count) + " verified objects.")
        #Close file
        f.close()


'''
TAKEN FROM TEST.JSON - 002.jpg

,
"1":
{
"shape_attributes":
{
"name":"rect",
"x":76,
"y":133,
"width":68,
"height":207
},
"region_attributes":
{
"object":"blah"
}
}

'''
