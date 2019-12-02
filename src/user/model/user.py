from .username import Username
from .fullname import Fullname
from .usermail import UserMail
from .userId import UserId
from .password import Password


class User():

    def __init__(self, userid: UserId, username: Username, userMail: UserMail, userFullname: Fullname, password: Password):
        self.__userId: UserId = userid
        self.__userName: Username = username
        self.__fullName: UserFullName = userFullname
        self.__email: UserMail = userMail
        self.__password: Password = password

    @property
    def userId(self):
        return self.__userId.value

    @property
    def username(self):
        return self.__userName.value

    @property
    def fullname(self):
        return self.__fullName.value

    @property
    def email(self):
        return self.__email.value

    @property
    def password(self):
        return self.__password.value

    def verifyPassword(self, password: str):
        return self.__password.verify(password)

    #####
    # Flask-login methods
    #####
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.__userId.value