class Schedule:
    def __init__(self):
        self.classes = []

    def get_classes(self):
        return self.classes

    def get_one(self, num):
        return self.classes[num - 1]

    def change_class(self, num, name):
        self.classes[num - 1] = name
