import unittest
from ..postCommentContent import PostCommentContent


class TestPostCommentContent(unittest.TestCase):

    def test_constructor(self):
        content = PostCommentContent("Post Content")

        expectedValue = PostCommentContent
        value = type(content)

        self.assertEqual(value, expectedValue)
    

    def test_value(self):
        content = PostCommentContent("Post Content")

        expectedValue = "Post Content"
        value = content.value

        self.assertEqual(value, expectedValue)


    def test_formString_constructor(self):
        content = PostCommentContent.fromString("Post Content")

        expectedValue = PostCommentContent
        value = type(content)

        self.assertEqual(value, expectedValue)
