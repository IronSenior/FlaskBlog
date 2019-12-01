from .postTitle import PostTitle
from .postSubtitle import PostSubtitle
from .postContent import PostContent
from .postId import PostId
from src.user.model.userId import UserId


class Post():

    def __init__(self, postid: PostId, userid: UserId, title: PostTitle, subtitle: PostSubtitle, content: PostContent):
        self.__postId: PostId = postid
        self.__userId: UserId = userid
        self.__title: PostTile = title
        self.__subtitle: PostSubtitle = subtitle
        self.__content: PostContent = content


    # This function should be in repository
    @staticmethod
    def fromSortedStringTuple(post: tuple):
        Post.__checkTupleSize(post)
        return Post(
            postid = PostId.fromString(post[0]),
            userid = UserId.fromString(post[1]),
            title = PostTitle.fromString(post[2]),
            subtitle = PostSubtitle.fromString(post[3]),
            content = PostContent.fromString(post[4])
        )
    
    @staticmethod
    def __checkTupleSize(post: tuple):
        if len(post) != 5:
            raise ValueError("Post Tuple is not well made")
    
    @property
    def postid(self):
        return self.__postId.value

    @property
    def userid(self):
        return self.__userId.value

    @property
    def title(self):
        return self.__title.value

    @property
    def subtitle(self):
        return self.__subtitle.value

    @property
    def content(self):
        return self.__content.value

    