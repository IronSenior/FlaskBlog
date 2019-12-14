import sqlalchemy as db
import os
import pandas
from uuid import UUID

engine = db.create_engine(os.environ["DB_ENGINE"])
connection = engine.connect()
metadata = db.MetaData()


def create_user_table():
    users = db.Table('users', metadata,
                db.Column('userid', db.String(36), nullable=False),
                db.Column('username', db.String(255), nullable=False),
                db.Column('fullname', db.String(255), nullable=False),
                db.Column('email', db.String(255), nullable=False),
                db.Column('password', db.String(255), nullable=False)
            )     
    

def create_post_table():
    posts = db.Table('posts', metadata,
                db.Column('postid', db.String(36), nullable=False),
                db.Column('userid', db.String(36), nullable=False),
                db.Column('title', db.String(255), nullable=False),
                db.Column('subtitle', db.String(255), nullable=False),
                db.Column('content', db.String(5000), nullable=False),
            )


def create_comment_table():
    comments = db.Table('comments', metadata,
                db.Column('commentid', db.String(36), nullable=False),
                db.Column('userid', db.String(36), nullable=False),
                db.Column('postid', db.String(36), nullable=False),
                db.Column('username', db.String(255), nullable=False),
                db.Column('content', db.String(1000), nullable=False),
                db.Column('parentid', db.String(36), nullable=True),
            )


if __name__ == "__main__":
    create_user_table()
    create_post_table()
    create_comment_table()
    metadata.create_all(engine)