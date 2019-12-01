


class PostTitle():
    
    def __init__(self, title: str):
        self.__value = title
    
    @staticmethod
    def fromString(title: str):
        return PostTitle(title)

    @property
    def value(self):
        return self.__value