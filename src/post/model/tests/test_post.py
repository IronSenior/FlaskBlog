import unittest
import uuid
from src.user.model.userId import UserId
from ..post import Post
from ..postId import PostId
from ..postTitle import PostTitle
from ..postSubtitle import PostSubtitle
from ..postContent import PostContent

class TestPost(unittest.TestCase):

    def test_constructor(self):
        postid = PostId(uuid.uuid4())
        userid = UserId(uuid.uuid4())
        title = PostTitle.fromString("Post Title")
        subtitle = PostSubtitle.fromString("Post Subtitle")
        content = PostContent.fromString("Post Content")
        
        post = Post(postid, userid, title, subtitle, content)

        expectedValue = Post
        value = type(post)

        self.assertEqual(value, expectedValue)


    def test_tuple_constructor(self):
        postTuple = (
            str(uuid.uuid4()),
            str(uuid.uuid4()),
            "Post Title",
            "Post Subtitle",
            "Post Content"
        )
        post = Post.fromSortedStringTuple(postTuple)

        expectedValue = Post
        value = type(post)

        self.assertEqual(value, expectedValue)
