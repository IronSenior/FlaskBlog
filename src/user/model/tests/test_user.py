from ..user import User
from ..username import Username
from ..usermail import UserMail
from ..fullname import Fullname
from ..userId import UserId
import unittest
import uuid


class TestUser(unittest.TestCase):

    def test_constructor(self):
        userid = UserId(uuid.uuid4())
        username = Username("IronSenior")
        usermail = UserMail("plokiju@gmail.com")
        fullname = Fullname("Jose Marquez Doblas")

        expectedValue = User
        value = User(userid, username, usermail, fullname)
        
        self.assertEqual(type(value), expectedValue)
