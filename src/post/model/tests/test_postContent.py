import unittest
from ..postContent import PostContent


class TestPostContent(unittest.TestCase):

    def test_constructor(self):
        content = PostContent("Post Content")

        expectedValue = PostContent
        value = type(content)

        self.assertEqual(value, expectedValue)
    

    def test_value(self):
        content = PostContent("Post Content")

        expectedValue = "Post Content"
        value = content.value

        self.assertEqual(value, expectedValue)


    def test_formString_constructor(self):
        content = PostContent.fromString("Post Content")

        expectedValue = PostContent
        value = type(content)

        self.assertEqual(value, expectedValue)
