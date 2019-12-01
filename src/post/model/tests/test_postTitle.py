import unittest
from ..postTitle import PostTitle


class TestPostTitle(unittest.TestCase):

    def test_constructor(self):
        title = PostTitle("Post Title")

        expectedValue = PostTitle
        value = type(title)

        self.assertEqual(value, expectedValue)
    

    def test_value(self):
        title = PostTitle("Post Title")

        expectedValue = "Post Title"
        value = title.value

        self.assertEqual(value, expectedValue)


    def test_formString_constructor(self):
        title = PostTitle.fromString("Post Title")

        expectedValue = PostTitle
        value = type(title)

        self.assertEqual(value, expectedValue)
