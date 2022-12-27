from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    images = relationship('Images', back_populates='owner')


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("Users", back_populates='users')
