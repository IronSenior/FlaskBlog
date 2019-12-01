


class PostCommentContent():
    
    def __init__(self, content: str):
        self.__value = content

    
    @staticmethod
    def fromString(content: str):
        return PostCommentContent(content)

    @property
    def value(self):
        return self.__value