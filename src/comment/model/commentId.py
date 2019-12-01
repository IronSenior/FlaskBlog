import uuid
from uuid import UUID

class CommentId():

    def __init__(self, commentid: UUID):
        self.checkUniqueId(commentid)
        self.checkIdVersion(commentid)
        self.__value: UUID = commentid

    @staticmethod
    def fromString(commentid: str):
        return CommentId(UUID(commentid))
    
    @property
    def value(self):
        return self.__value
    
    def checkUniqueId(self, commentid: UUID):
        if type(commentid) != UUID:
            raise TypeError("User ID must be an UUID instance")

    def checkIdVersion(self, commentid: UUID):
        if commentid.version != 4:
            raise TypeError("User ID must be version 4")