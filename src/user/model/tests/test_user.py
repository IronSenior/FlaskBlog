from ..user import User
from ..username import Username
from ..usermail import UserMail
from ..fullname import Fullname
from ..userId import UserId
from ..password import Password
from passlib.hash import sha256_crypt
import unittest
import uuid


class TestUser(unittest.TestCase):

    def test_constructor(self):
        userid = UserId(uuid.uuid4())
        username = Username.fromString("IronSenior")
        usermail = UserMail.fromString("plokiju@gmail.com")
        fullname = Fullname.fromString("Jose Marquez Doblas")
        password = Password.fromString("password")

        expectedValue = User
        value = User(userid, username, usermail, fullname, password)
        
        self.assertEqual(type(value), expectedValue)
        
    def test_it_can_verify_password(self):
        userid = UserId(uuid.uuid4())
        username = Username.fromString("IronSenior")
        usermail = UserMail.fromString("plokiju@gmail.com")
        fullname = Fullname.fromString("Jose Marquez Doblas")
        password = Password.fromString("password")

        user = User(userid, username, usermail, fullname, password)

        self.assertTrue(user.verifyPassword("password"))
        self.assertFalse(user.verifyPassword("notpassword"))