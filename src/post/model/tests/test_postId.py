import unittest
import uuid
from uuid import UUID
from ..postId import PostId


class TestPostId(unittest.TestCase):

    def test_constructor(self):
        uniqueId = uuid.uuid4()
        postid = PostId(uniqueId)
        self.assertEqual(postid.value, uniqueId)

    def test_from_string_constructor(self):
        uniqueId = str(uuid.uuid4())
        postid = PostId.fromString(uniqueId)
        self.assertEqual(postid.value, UUID(uniqueId))

    def test_string_id(self):
        with self.assertRaises(TypeError):
            postid = PostId("24")

    def test_non_integer_usermail(self):
        with self.assertRaises(TypeError):
            postid = PostId(23.4)