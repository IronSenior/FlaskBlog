import unittest
import uuid
from uuid import UUID
from ..commentId import CommentId

class TestCommentId(unittest.TestCase):

    def test_constructor(self):
        uniqueId = uuid.uuid4()
        commentid = CommentId(uniqueId)
        self.assertEqual(commentid.value, uniqueId)

    def test_from_string_constructor(self):
        uniqueId = str(uuid.uuid4())
        commentid = CommentId.fromString(uniqueId)
        self.assertEqual(commentid.value, UUID(uniqueId))

    def test_string_id(self):
        with self.assertRaises(TypeError):
            commentid = CommentId("24")

    def test_non_integer_id(self):
        with self.assertRaises(TypeError):
            commentid = CommentId(23.4)