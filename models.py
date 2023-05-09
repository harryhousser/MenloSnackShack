from sqlalchemy import ForeignKey, Column, INTEGER, TEXT, BOOLEAN, DATETIME
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    # Columns
    username = Column('username', TEXT, primary_key=True)
    password = Column('password', TEXT, nullable=False)
    is_admin = Column('is_admin', BOOLEAN, default=False)


    snacks = relationship('Snack', back_populates='user')




class Snack(Base):
    __tablename__ = "snacks"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    name = Column("name", TEXT, nullable=False)
    category = Column("category", TEXT, nullable=False)
    image = Column("image", TEXT, nullable=False)
    link = Column("link", TEXT, nullable=False)
    like_count = Column("like_count", INTEGER, default=0)
    user_id = Column("user_id", INTEGER, ForeignKey("users.username"))

    # Relationships
    user = relationship("User", back_populates="snacks")



# snacks



#todo

