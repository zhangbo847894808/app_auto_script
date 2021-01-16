import os, yaml


class Read_data:
    def __init__(self, filename):
        self.filename = os.getcwd() + os.sep + "Data" + os.sep +filename + ".yaml"

    def load_data(self):
        with open(self.filename, 'r', encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data
