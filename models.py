# Use these as class for the Table declaration and creation
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship

from database import Base


class File(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    user_ids = relationship("UserId", back_populates="files")
    content = Column(String, index=True)

class UserId(Base):
    __tablename__ = "user_id"

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("file.id"))
    files = relationship("File", back_populates="user_ids")
