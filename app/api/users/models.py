from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from database import Base

class DictMixIn:
  def to_dict(self):
      return {
          column.name: getattr(self, column.name)
          for column in self.__table__.columns
      }

class User(Base, DictMixIn):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, index=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    books = relationship('Book', backref='users.id')

    def __init__(self, id, username, email):
      self.id = id
      self.username = username
      self.email = email

    def __repr__(self):
        return '%d' % self.id