import uuid
import os
import sqlalchemy as db
from uuid import UUID
from ..model.user import User
from ..model.usermail import UserMail
from ..model.userId import UserId

class UserRepository():

    def __init__(self):
        self.__engine = db.create_engine(os.environ['DB_ENGINE'])
        self.__conection = self.__engine.connect()
        self.__metadata = db.MetaData()
        self.__users = db.Table("users", self.__metadata, autoload=True, autoload_with=self.__engine)

    def getById(self, userid: UUID):
        query = db.select([self.__users]).where(self.__users.columns.userid == userid)
        resultProxy = self.__conection.execute(query)
        resultSet = resultProxy.fetchall()
        return User.fromSortedStringTuple(resultSet[0])

    def getByEmail(self, email: UserMail):
        query = db.select([self.__users]).where(self.__users.columns.email == email.value)
        resultProxy = self.__conection.execute(query)
        resultSet = resultProxy.fetchall()
        return User.fromSortedStringTuple(resultSet[0])

    def add(self, user: User):
        query = db.insert(self.__users).values(userid=user.userId, username=user.username, fullname=user.fullname, email=user.email, password=user.password)
        resultProxy = self.__conection.execute(query)
    
    def delete(self, user: User):
        query = db.delete(self.__users).where(self.__users.columns.userid == user.userId)
        resultProxy = self.__conection.execute(query)

    def update(self, user: User):
        query = db.update(self.__users).values(username=user.username, fullname=user.fullname, email=user.email, password=user.password).where(self.__users.columns.userid == user.userId)
        resultProxy = self.__conection.execute(query)
    
