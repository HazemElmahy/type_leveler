from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Numeric, Integer


Base = declarative_base()

class Speed(Base):
    __tablename__ = "speed"

    id = Column(Integer, primary_key=True, index=True)
    speed = Column(Integer)
    state = Column(Integer)


class Accuracy(Base):
    __tablename__ = "accuracy"

    id = Column(Integer, primary_key=True, index=True)
    accuracy =  Numeric(Integer)
    state = Column(Integer)