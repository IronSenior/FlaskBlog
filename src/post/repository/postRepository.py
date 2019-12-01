import uuid
import os
import sqlalchemy as db
from uuid import UUID
from ..model.post import Post

class UserRepository():

    def __init__(self):
        self.__engine = db.create_engine(os.environ['DB_ENGINE'])
        self.__conection = self.__engine.connect()
        self.__metadata = db.MetaData()
        self.__posts = db.Table("posts", self.__metadata, autoload=True, autoload_with=self.__engine)

    def getById(self, postid: UUID):
        query = db.select([self.__posts]).where(self.__posts.columns.postid == postid)
        resultProxy = self.__conection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return None
        return Post.fromSortedStringTuple(resultSet[0])

    def add(self, post: Post):
        query = db.insert(self.__posts).values(postid=post.postid, userid=post.userid, title=post.title, subtitle=post.subtitle, content=post.content)
        resultProxy = self.__conection.execute(query)

    def delete(self, post: Post):
        query = db.delete(self.__posts).where(self.__posts.columns.postid == post.postid)
        resultProxy = self.__conection.execute(query)

    def update(self, post: Post):
        query = db.update(self.__posts).values(title=post.title, subtitle=post.subtitle, content=post.content).where(self.__posts.columns.postid == post.postid)
        resultProxy = self.__conection.execute(query)
