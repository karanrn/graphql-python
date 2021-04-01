from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class DictMixIn:
  def to_dict(self):
      return {
          column.name: getattr(self, column.name)
          for column in self.__table__.columns
      }

class Book(Base, DictMixIn):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(256), index=True, nullable=False)
    description = Column(Text, nullable=False)
    year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '' % self.title % self.description % self.year % self.author_id