import unittest
import uuid
from ..comment import Comment
from ..commentContent import CommentContent
from ..commentId import CommentId
from src.user.model.userId import UserId
from src.post.model.postId import PostId


class TestComment(unittest.TestCase):


    def test_constructor(self):
        comment = Comment(CommentId(uuid.uuid4()), UserId(uuid.uuid4()), PostId(uuid.uuid4()), CommentContent.fromString("Muy bueno tu post"))

        expectedValue = Comment
        value = type(comment)

        self.assertEqual(value, expectedValue)

        
    def test_content(self):
        comment = Comment(CommentId(uuid.uuid4()), UserId(uuid.uuid4()), PostId(uuid.uuid4()), CommentContent.fromString("Muy bueno tu post"))

        expectedValue = "Muy bueno tu post"
        value = comment.content

        self.assertEqual(value, expectedValue)

