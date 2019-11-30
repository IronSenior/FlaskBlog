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


    def test_tuple_constructor(self):
        user_tuple = (str(uuid.uuid4()), "Pepe", "Jose Marquez", "pepemarquezof@gmail.com")

        expectedValue = User
        value = User.fromSortedStringTuple(user_tuple)

        self.assertEqual(type(value), expectedValue)
