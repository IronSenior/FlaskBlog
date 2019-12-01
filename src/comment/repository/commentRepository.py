from ..model.comment import Comment
import uuid
from uuid import UUID
import os
import sqlalchemy as db


class CommentRepository():

    def __init__(self):
        self.__engine = db.create_engine(os.environ['DB_ENGINE'])
        self.__conection = self.__engine.connect()
        self.__metadata = db.MetaData()
        self.__comments = db.Table("comments", self.__metadata, autoload=True, autoload_with=self.__engine)

    
    def getById(self, commentid: UUID):
        query = db.select([self.__comments]).where(self.__comments.columns.commentid == commentid)
        resultProxy = self.__conection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return None
        return Comment.fromSortedStringTuple(resultSet[0])

    def add(self, comment: Comment):
        query = db.insert(self.__comments).values()
        resultProxy = self.__conection.execute(query)

    def delete(self, comment: Comment):
        query = db.delete(self.__comments).where(self.__comments.columns.commentid == comment.commentid)
        resultProxy = self.__conection.execute(query)

    def update(self, comment: Comment):
        query = db.update(self.__comments).values().where(self.__comments.columns.commentid == comment.commentid)
        resultProxy = self.__conection.execute(query)