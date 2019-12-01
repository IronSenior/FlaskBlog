

class PostContent():
    
    def __init__(self, content: str):
        self.__value = content

    
    @staticmethod
    def fromString(content: str):
        return PostContent(content)

    @property
    def value(self):
        return self.__value