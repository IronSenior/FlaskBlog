import re

class UserMail():

    def __init__(self, usermail: str):
        self.checkIsMail(usermail)
        self.__value = usermail

    @staticmethod
    def fromString(usermail: str):
        return UserMail(usermail)
    
    @property
    def value(self):
        return self.__value
    
    def checkIsMail(self, usermail):
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", usermail):
            raise ValueError()