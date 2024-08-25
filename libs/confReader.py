import json

class confReader(object):
    def __init__(self):
        self.loadJson()

    def loadJson(self):
        f=open("configuration.json")
        data=json.load(f)
        print(data)
        f.close()