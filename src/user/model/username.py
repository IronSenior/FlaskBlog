# src/models/user/username.py

class Username():

    def __init__(self, username: str):
        self.__checkUsernameLenght(username)
        self.__checkUsernameSpaces(username)
        self.__value: str = username;

    def __checkUsernameLenght(self, username: str):
        if len(username) == 0:
            raise ValueError()

    def __checkUsernameSpaces(self, username: str):
        if " " in username:
            raise ValueError()

    @staticmethod
    def fromString(username: str):
        return Username(username)

    @property
    def value(self):
        return self.__value