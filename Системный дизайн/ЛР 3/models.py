from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)

    folders = relationship("Folder", back_populates="user")

class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="folders")
    messages = relationship("Message", back_populates="folder")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    content = Column(Text)
    sender = Column(String)
    recipient = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    folder_id = Column(Integer, ForeignKey("folders.id", ondelete="CASCADE"))

    folder = relationship("Folder", back_populates="messages")
