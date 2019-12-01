import unittest
import uuid
from ..postComment import PostComment
from ..postCommentContent import PostCommentContent
from src.user.model.userId import UserId


class TestPostComment(unittest.TestCase):


    def test_constructor(self):
        comment = PostComment(UserId(uuid.uuid4()), PostCommentContent.fromString("Muy bueno tu post"))

        expectedValue = PostComment
        value = type(comment)

        self.assertEqual(value, expectedValue)

        
    def test_content(self):
        comment = PostComment(UserId(uuid.uuid4()), PostCommentContent.fromString("Muy bueno tu post"))

        expectedValue = "Muy bueno tu post"
        value = comment.value

        self.assertEqual(value, expectedValue)
