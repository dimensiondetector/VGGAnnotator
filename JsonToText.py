import json

with open('test.json') as json_data:
    data = json.load(json_data) #load test json data
    #print ( data)

    #for r in data['10548720_809096559166869_7732497753236727840_o.jpg459203']:

    for p in data:
        r = data[p]
        for q in r['regions']:
            s = r['regions'][q]
            print "FUCK YES"
            for m in s['shape_attributes']:
                n = s['shape_attributes'][m]
                if (n != "rect"):
                    print(n)
