import sqlalchemy as db

import uuid
from uuid import UUID
import os

from ...user.model.userId import UserId
from ...user.model.username import Username
from ...post.model.postId import PostId
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
        query = db.insert(self.__comments).values(commentid=comment.commentid, userid=comment.userid, postid=comment.postid, username=comment.username, content=comment.content, parentid=comment.parentid)
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
            username=Username.fromString(result[3]),
            content=CommentContent.fromString(result[4]),
            parentid= CommentId.fromString(result[5]) if result[5] else None
        )
    
    def getByPost(self, postid: UUID):
        query = db.select([self.__comments]).where(self.__comments.columns.postid == postid).where(self.__comments.columns.parentid == None)
        resultProxy = self.__conection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return None
        comments = []
        for comment in resultSet:
            comments.append(self.__getCommentFromResult(comment))

        comments = self.__reagrupate_comments(comments)
        return comments


    def __reagrupate_comments(self, comments: list):
        final_comments = []
        for comment in comments:
            final_comments.append({
                'parent': comment,
                'children': self.getByParent(comment.commentid)
            })
        return final_comments


    def getByParent(self, parentid: UUID):
        query = db.select([self.__comments]).where(self.__comments.columns.parentid == parentid)
        resultProxy = self.__conection.execute(query)
        resultSet = resultProxy.fetchall()

        comments = []
        for comment in resultSet:
            comments.append(self.__getCommentFromResult(comment))
        
        comments = self.__reagrupate_comments(comments)
        return comments