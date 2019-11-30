import uuid
import os
import sqlalchemy as db
from uuid import UUID
from ..model.user import User

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
        return resultSet

    def add(self, user: User):
        pass
    
    def delete(self, user: User):
        pass

    def update(self, user: User):
        pass
    
