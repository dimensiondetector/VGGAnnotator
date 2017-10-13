import json

objects = {
    'car': 1,
    'truck': 2,
    'streetsign': 3, #ex.stop sign
    'trafficlight': 4, #red,yellow,green
    'person': 5,
    'door' : 6,
    'window' : 7,
    'building': 8
}

with open('test.json') as json_data:
    jsonfile = json.load(json_data)

    for parameters in jsonfile:
        #Read each parameter in the JSON
        parameterList = jsonfile[parameters]

        #Retreive filename and create filename string for text file
        imagename = parameterList['filename']
        nameString = parameterList['filename']
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
  
        
        #Boolean to tell if first value in text file
        firstLine = True

        #Get each square drawn in that picture
        for square in parameterList['regions']:
            specificSquare = parameterList['regions'][square]
            objectName = specificSquare['region_attributes']['object']

            if objectName not in objects:
                print("\nError in: " + imagename)
                print("Did not create file: " + nameString)
                print("Object name - " + objectName + " - does not match a known object.\n")
            else:
                #Create text file with write capabilities
                f = open(nameString, 'w')
			    #f.open()
			    
                print("\n-----")
                print(objectName)
                print("-----\n")

                if (firstLine == True):
					objectCompare =objectName.lower()
				    f.write(objects[objectCompare]) #f.write(objectName)                                                            
                    firstLine = False
                #If object name is not the first object for this image print the name on a new line
                else:
                    if specificSquare['shape_attributes']['name'] != "rect":
                        print("Error in file: " + nameString)
                        print("Object: " + objectName + "does not follow rectangle format.")
                    else:
                        f.write("\n" + objects[objectCompare])

                        #Obtain square-object x y width and height attributes
                        for objectDetails in specificSquare['shape_attributes']:
                            objectDimensions = specificSquare['shape_attributes'][objectDetails]
                            if (objectDimensions != "rect"):
                                f.write(" " + str(objectDimensions))
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
