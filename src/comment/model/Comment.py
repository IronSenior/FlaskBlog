from src.user.model.userId import UserId
from .postCommentContent import PostCommentContent


class PostComment():
    
    def __init__(self, userid: UserId, content: PostCommentContent):
        self.__userid: UserId = userid
        self.__content: PostCommentContent = content
    
    @property
    def value(self):
        return self.__content.value