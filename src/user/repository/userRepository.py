import sqlalchemy as db

import uuid
from uuid import UUID
import os

from ..model.user import User
from ..model.username import Username
from ..model.fullname import Fullname
from ..model.usermail import UserMail
from ..model.userId import UserId
from ..model.password import Password

class UserRepository():

    def __init__(self):
        self.__engine = db.create_engine(os.environ['DB_ENGINE'])
        self.__conection = self.__engine.connect()
        self.__metadata = db.MetaData()
        self.__users = db.Table("users", self.__metadata, autoload=True, autoload_with=self.__engine)

    def add(self, user: User):
        query = db.insert(self.__users).values(userid=user.userId, username=user.username, fullname=user.fullname, email=user.email, password=user.password)
        resultProxy = self.__conection.execute(query)
    
    def delete(self, user: User):
        query = db.delete(self.__users).where(self.__users.columns.userid == user.userId)
        resultProxy = self.__conection.execute(query)

    def update(self, user: User):
        query = db.update(self.__users).values(username=user.username, fullname=user.fullname, email=user.email, password=user.password).where(self.__users.columns.userid == user.userId)
        resultProxy = self.__conection.execute(query)

    def getById(self, userid: UUID):
        query = db.select([self.__users]).where(self.__users.columns.userid == userid)
        resultProxy = self.__conection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return None
        return self.__getUserFromResult(resultSet[0])

    def getByEmail(self, email: UserMail):
        query = db.select([self.__users]).where(self.__users.columns.email == email.value)
        resultProxy = self.__conection.execute(query)
        resultSet = resultProxy.fetchall()
        if not resultSet:
            return None
        return self.__getUserFromResult(resultSet[0])

    def __getUserFromResult(self, result: tuple):
        return User(
            userid = UserId.fromString(result[0]),
            username = Username.fromString(result[1]),
            userFullname= Fullname.fromString(result[2]),
            userMail = UserMail.fromString(result[3]),
            password = Password(result[4]) 
        )




    
