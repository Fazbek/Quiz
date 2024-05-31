from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    level = Column(String, default="Select your level", nullable=False)
    datetime = Column(DateTime)


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, nullable=False)
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(Integer, nullable=False)
    timer = Column(DateTime)



