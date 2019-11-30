

class Fullname():

    def __init__(self, fullname: str):
        self.checkFullnameLenght(fullname)
        self.__value = fullname

    @staticmethod
    def fromString(fullname: str):
        return Fullname(fullname)

    @property
    def value(self):
        return self.__value

    def checkFullnameLenght(self, fullname: str):
        if len(fullname) == 0:
            raise ValueError()
