from .username import Username
from .fullname import Fullname
from .usermail import UserMail
from .userId import UserId

class User():

    def __init__(self, userid: UserId, username: Username, userMail: UserMail, userFullname: Fullname = None):
        self.__userId: userid
        self.__userName: Username = username
        self.__fullName: UserFullName = userFullname
        self.__email: UserMail = userMail

    @property
    def username(self):
        return self.__username.value

    @property
    def fulname(self):
        return self.__fullname.value

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