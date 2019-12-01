import unittest
from ..postSubtitle import PostSubtitle


class TestPostSubtitle(unittest.TestCase):

    def test_constructor(self):
        subtitle = PostSubtitle("Post SubTitle")

        expectedValue = PostSubtitle
        value = type(subtitle)

        self.assertEqual(value, expectedValue)
    

    def test_value(self):
        subtitle = PostSubtitle("Post SubTitle")

        expectedValue = "Post SubTitle"
        value = subtitle.value

        self.assertEqual(value, expectedValue)


    def test_formString_constructor(self):
        subtitle = PostSubtitle.fromString("Post SubTitle")

        expectedValue = PostSubtitle
        value = type(subtitle)

        self.assertEqual(value, expectedValue)
