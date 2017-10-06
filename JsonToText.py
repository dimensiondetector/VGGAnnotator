import json

with open('test.json') as json_data:
    jsonfile = json.load(json_data)

    for parameters in jsonfile:
        #Read each parameter in the JSON
        parameterList = jsonfile[parameters]

        #Retreive filename and create filename string for text file
        nameString = parameterList['filename']
        nameString = nameString.replace(".jpg", ".txt")

        #Create text file with write capabilities
        f = open(nameString, 'w')

        #Boolean to tell if first value in text file
        firstLine = True

        #Get each square drawn in that picture
        for square in parameterList['regions']:
            specificSquare = parameterList['regions'][square]

            #
            for objectIdentifier in specificSquare['region_attributes']:
                objectName = specificSquare['region_attributes'][objectIdentifier]
                print("---")
                print(objectName)
                if (firstLine == True):
                    f.write(objectName)
                    firstLine = False
                else:
                    f.write("\n" + objectName)
                print("---")
            for objectDetails in specificSquare['shape_attributes']:
                objectDimensions = specificSquare['shape_attributes'][objectDetails]
                if (objectDimensions != "rect"):
                    print(objectDimensions)
                    f.write(" " + str(objectDimensions))
        f.close()
