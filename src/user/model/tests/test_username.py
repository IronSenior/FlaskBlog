import unittest
from ..username import Username

class TestUserName(unittest.TestCase):


    def test_correct_constructor(self):
        userName = Username("John")
        expectedValue = "John"
        self.assertEqual(userName.value, expectedValue)

    def test_from_string_constructor(self):
        userName = Username.fromString("Tanya")
        expectedValue = "Tanya"
        self.assertEqual(userName.value, expectedValue)

    def test_bad_name(self):
        with self.assertRaises(ValueError):
            userName = Username("")

    def test_username_with_spaces(self):
        with self.assertRaises(ValueError):
            userName = Username("John Cenna")