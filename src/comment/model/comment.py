from src.user.model.userId import UserId
from src.post.model.postId import PostId
from .commentContent import CommentContent
from .commentId import CommentId


class Comment():
    
    def __init__(self, commentid: CommentId, userid: UserId, postid: PostId, content: CommentContent, parentid: CommentId = None):
        self.__commentid: CommentId = commentid
        self.__userid: UserId = userid
        self.__postid: PostId = postid
        self.__parentid: CommentId = parentid
        self.__content: CommentContent = content
    

    @staticmethod
    def fromSortedStringTuple(commentTuple):
        return Comment(
            commentid=CommentId.fromString(commentTuple[0]),
            userid=UserId.fromString(commentTuple[1]),
            postid=PostId.fromString(commentTuple[2]),
            content=CommentContent.fromString(commentTuple[3])
        )

    @property
    def value(self):
        return self.__content.value

    @property
    def parentid(self):
        if not self.__parentid:
            return None
        return self.__parentid.value

    @property
    def userid(self):
        return self.__userid.value

    @property
    def postid(self):
        return self.__postid.value
    
    @property
    def commentid(self):
        return self.__commentid.value

    