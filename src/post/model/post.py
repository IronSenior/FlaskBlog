from .postTitle import PostTitle
from .postSubtitle import PostSubtitle
from .postContent import PostContent
from .postId import PostId
from ...user.model.userId import UserId


class Post():

    def __init__(self, postid: PostId, userid: UserId, title: PostTitle, subtitle: PostSubtitle, content: PostContent):
        self.__postId: PostId = postid
        self.__userId: UserId = userid
        self.__title: PostTile = title
        self.__subtitle: PostSubtitle = subtitle
        self.__content: PostContent = content

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

    