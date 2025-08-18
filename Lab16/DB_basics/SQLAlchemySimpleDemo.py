from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Create an engine to connect to a SQLite database
engine = create_engine("sqlite:///users.db")

# Declare a base using declarative_base
Base = declarative_base()


# Define the User class inheriting from Base
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Create the tables in the database
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

# session = Session()
with Session() as session:
    # Create a new user instance
    new_user = User(name="Ivan", age=30)

    # Add the new user to the session
    session.add(new_user)
    session.commit()
