import unittest
from ..usermail import UserMail


class TestUserMail(unittest.TestCase):

    def test_constructor(self):
        usermail = UserMail("plokiju@hotmail.com")
        expectedValue = "plokiju@hotmail.com"
        self.assertEqual(usermail.value, expectedValue)

    def test_from_string_constructor(self):
        usermail = UserMail.fromString("poiuy@hotmail.com")
        expectedValue = "poiuy@hotmail.com"
        self.assertEqual(usermail.value, expectedValue)

    def test_empty_mail(self):
        with self.assertRaises(ValueError):
            usermail = UserMail("")

    def test_bad_usermail(self):
        with self.assertRaises(ValueError):
            usermail = UserMail("John Cenna")