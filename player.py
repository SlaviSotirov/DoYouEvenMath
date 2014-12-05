from sqlalchemy import Column, Integer, String
from connection import Base


class Player(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

    def __str__(self):
        return "{} - {} points".format(self.name, self.score)

    def __repr__(self):
        return self.__str__()