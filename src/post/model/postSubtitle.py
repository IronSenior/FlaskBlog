class PostSubtitle():

    def __init__(self, subtitle: str):
        self.__value = subtitle

    @staticmethod
    def fromString(subtitle: str):
        return PostSubtitle(subtitle)

    @property
    def value(self):
        return self.__value