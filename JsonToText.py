import json

with open('test.json') as json_data:
    data = json.load(json_data)

    for params in data:
        parameterList = data[params]
        print(parameterList)
        for name in parameterList['filename']:
            print(name)
        for square in parameterList['regions']:
            specificSquare = parameterList['regions'][square]
            print(" \n YES")
            print("-------")
            print(specificSquare)
            print("-------")
            for k in specificSquare['region_attributes']:
                l = specificSquare['region_attributes'][k]
                print(l)
            for m in specificSquare['shape_attributes']:
                n = specificSquare['shape_attributes'][m]
                if (n != "rect"):
                    print(n)
