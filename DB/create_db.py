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
              db.Column('fullname', db.String(255)),
              db.Column('email', db.String(255), nullable=False)
              )
              
    metadata.create_all(engine) #Creates the table


if __name__ == "__main__":
    create_user_table()