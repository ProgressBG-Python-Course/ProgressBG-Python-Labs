from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import declarative_base

# Base class for our class definitions
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # Define the table name

    # Define the columns of the table
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String, nullable=False)   # Name cannot be null
    age = Column(Integer, nullable=False)   # Age cannot be null

    def __repr__(self):
        # Human-readable representation of the object, helpful for debugging
        return f"<User(name={self.name}, age={self.age})>"
