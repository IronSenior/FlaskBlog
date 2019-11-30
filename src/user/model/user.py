from .username import Username
from .fullname import Fullname
from .usermail import UserMail
from .userId import UserId

class User():

    def __init__(self, userid: UserId, username: Username, userMail: UserMail, userFullname: Fullname):
        self.__userId: UserId = userid
        self.__userName: Username = username
        self.__fullName: UserFullName = userFullname
        self.__email: UserMail = userMail

    @staticmethod
    def fromSortedStringTuple(user: tuple):
        return User(
            userid = UserId.fromString(user[0]),
            username = Username.fromString(user[1]),
            userFullname= Fullname.fromString(user[2]),
            userMail = UserMail.fromString(user[3]) 
        )

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