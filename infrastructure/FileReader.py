import json


class FileReader:
    def __init__(self, file_name):
        self.fileName = file_name

    def to_json(self):
        with open(self.fileName) as json_data:
            d = json.load(json_data)
            return d
