import unittest
from ..fullname import Fullname

class TestFullName(unittest.TestCase):

    def test_constructor(self):
        fullName = Fullname("John Alonso Prieto")
        expectedValue = "John Alonso Prieto"
        self.assertEqual(fullName.value, expectedValue)

    def test_from_string_constructor(self):
        fullName = Fullname.fromString("Tanya Alonso Prieto")
        expectedValue = "Tanya Alonso Prieto"
        self.assertEqual(fullName.value, expectedValue)

    def test_bad_name(self):
        with self.assertRaises(ValueError):
            userName = Fullname("")
