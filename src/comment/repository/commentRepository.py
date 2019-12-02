import sqlalchemy as db

import uuid
from uuid import UUID
import os

from src.user.model.userId import UserId
from src.post.model.postId import PostId
from ..model.comment import Comment
from ..model.commentId import CommentId
from ..model.commentContent import CommentContent


class CommentRepository():

    def __init__(self):
        self.__engine = db.create_engine(os.environ['DB_ENGINE'])
        self.__conection = self.__engine.connect()
        self.__metadata = db.MetaData()
        self.__comments = db.Table("comments", self.__metadata, autoload=True, autoload_with=self.__engine)

    def add(self, comment: Comment):
        query = db.insert(self.__comments).values(commentid=comment.commentid, userid=comment.userid, postid=comment.postid, content=comment.content, parentid=comment.parentid)
        resultProxy = self.__conection.execute(query)

    def delete(self, comment: Comment):
        query = db.delete(self.__comments).where(self.__comments.columns.commentid == comment.commentid)
        resultProxy = self.__conection.execute(query)

    def update(self, comment: Comment):
        query = db.update(self.__comments).values(content=comment.content).where(self.__comments.columns.commentid == comment.commentid)
        resultProxy = self.__conection.execute(query)

    def getById(self, commentid: UUID):
        query = db.select([self.__comments]).where(self.__comments.columns.commentid == commentid)
        resultProxy = self.__conection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return None
        return self.__getCommentFromResult(resultSet[0])

    def __getCommentFromResult(self, result: tuple):
        return Comment(
            commentid=CommentId.fromString(result[0]),
            userid=UserId.fromString(result[1]),
            postid=PostId.fromString(result[2]),
            content=CommentContent.fromString(result[3]),
            parentid= CommentId.fromString(result[4]) if result[4] else None
        )

