import unittest
from ..commentContent import CommentContent


class TestCommentContent(unittest.TestCase):

    def test_constructor(self):
        content = CommentContent("Comment Content")

        expectedValue = CommentContent
        value = type(content)

        self.assertEqual(value, expectedValue)
    

    def test_value(self):
        content = CommentContent("Comment Content")

        expectedValue = "Comment Content"
        value = content.value

        self.assertEqual(value, expectedValue)


    def test_formString_constructor(self):
        content = CommentContent.fromString("Comment Content")

        expectedValue = CommentContent
        value = type(content)

        self.assertEqual(value, expectedValue)
