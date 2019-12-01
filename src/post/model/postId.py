import uuid
from uuid import UUID

class PostId():

    def __init__(self, postid: UUID):
        self.checkUniqueId(postid)
        self.checkIdVersion(postid)
        self.__value: UUID = postid

    @staticmethod
    def fromString(postid: str):
        return PostId(UUID(postid))
    
    @property
    def value(self):
        return self.__value
    
    def checkUniqueId(self, postid: UUID):
        if type(postid) != UUID:
            raise TypeError("User ID must be an UUID instance")

    def checkIdVersion(self, postid: UUID):
        if postid.version != 4:
            raise TypeError("User ID must be version 4")